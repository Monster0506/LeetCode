import time
import traceback
from pprint import pformat
from typing import Any, Callable, Dict, List, Tuple, Type, Optional
import difflib
import threading

# ANSI escape codes for colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"


class TimeoutError(Exception):
    """Custom exception for test case timeouts."""

    pass


def _format_value(value: Any) -> str:
    """Formats a value for display, using pformat for complex types."""
    if isinstance(value, (str, int, float, bool, type(None))):
        return repr(value)
    return pformat(value, indent=2, width=60)


def _get_diff(expected: Any, actual: Any) -> str:
    """Generates a diff string for two values."""
    expected_str = pformat(expected, indent=2, width=60).splitlines()
    actual_str = pformat(actual, indent=2, width=60).splitlines()
    diff = difflib.unified_diff(
        expected_str,
        actual_str,
        fromfile="Expected",
        tofile="Actual",
        lineterm="",
    )
    return "\n".join(diff)


class _TimedCall:
    """Helper class to run a function with a timeout."""

    def __init__(
        self,
        func: Callable,
        args: Tuple,
        kwargs: Dict,
        setup: Optional[Callable] = None,
        teardown: Optional[Callable] = None,
    ):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.setup = setup
        self.teardown = teardown
        self.result: Any = None
        self.exception: Optional[BaseException] = None
        self.traceback_str: Optional[str] = None
        self._setup_exception: Optional[BaseException] = None
        self._setup_traceback: Optional[str] = None
        self._teardown_exception: Optional[BaseException] = None
        self._teardown_traceback: Optional[str] = None

    def _target(self):
        try:
            if self.setup:
                try:
                    self.setup()
                except Exception as e_setup:
                    self._setup_exception = e_setup
                    self._setup_traceback = traceback.format_exc()
                    # If setup fails, we might not want to run the main function or teardown
                    # For now, we'll record and let the main logic decide.
                    # Or, re-raise to stop here. Let's re-raise.
                    raise
            self.result = self.func(*self.args, **self.kwargs)
        except Exception as e_main:
            self.exception = e_main
            self.traceback_str = traceback.format_exc()
        finally:
            if self.teardown:
                try:
                    self.teardown()
                except Exception as e_teardown:
                    self._teardown_exception = e_teardown
                    self._teardown_traceback = traceback.format_exc()
                    # If teardown fails, we should report it.
                    # If main func also failed, this adds to the error info.

    def run(
        self, timeout_seconds: Optional[float]
    ) -> Tuple[Any, Optional[BaseException], Optional[str]]:
        thread = threading.Thread(target=self._target)
        thread.daemon = True  # So main program can exit
        thread.start()
        thread.join(timeout_seconds)

        if self._setup_exception:  # Setup failed before timeout check
            return None, self._setup_exception, self._setup_traceback

        if thread.is_alive():  # Timeout occurred
            # Note: The thread is still alive and might complete later.
            # This timeout is non-preemptive for CPU-bound tasks.
            return (
                None,
                TimeoutError(f"Execution exceeded timeout of {timeout_seconds}s"),
                None,
            )

        # Collect teardown errors if any
        if self._teardown_exception and not self.exception:
            # If main function was fine, but teardown failed, report teardown error
            return self.result, self._teardown_exception, self._teardown_traceback
        elif self._teardown_exception and self.exception:
            # If both main and teardown failed, append teardown info to main error
            self.traceback_str = f"{self.traceback_str}\n\n--- Teardown Error ---\n{self._teardown_traceback}"

        return self.result, self.exception, self.traceback_str


def run_leetcode_tests(
    solution_class: Type,
    method_name: str,
    test_cases: List[Dict[str, Any]],
    default_timeout: Optional[float] = None,  # Default timeout for all tests
) -> Dict[str, float]:
    """
    Runs a suite of LeetCode-style test cases against a solution method.

    Args:
        solution_class: The class containing the solution method.
        method_name: The name of the method to test.
        test_cases: A list of dictionaries, each representing a test case.
            Each test case can have:
            - 'name' (str, optional): Descriptive name.
            - 'args' (tuple, optional): Positional arguments. Defaults to ().
            - 'kwargs' (dict, optional): Keyword arguments. Defaults to {}.
            - 'expected' (any): Expected output. (Not used if 'expected_exception' is set).
            - 'expected_exception' (Type[BaseException], optional): Expected exception type.
            - 'comparator' (Callable[[Any, Any], bool], optional): Custom comparison function.
            - 'sort_output_before_compare' (bool, optional): Sort list outputs before comparing.
            - 'output_arg_index' (int, optional): Index of 'args' to use as actual output
                                                  for in-place modification testing.
            - 'timeout' (float, optional): Override default_timeout for this specific test case.
            - 'setup' (Callable[[], None], optional): Function to run before this test.
            - 'teardown' (Callable[[], None], optional): Function to run after this test.
        default_timeout (float, optional): Default timeout in seconds for each test case.
    """
    if not hasattr(solution_class, method_name):
        print(
            f"{RED}Error: Method '{method_name}' not found in class '{solution_class.__name__}'.{RESET}"
        )
        return {
            "total_cases": len(test_cases),
            "passed": len(test_cases),
            "failed": len(test_cases),
            "errors": len(test_cases),
            "total_time_ms": 0.000,
        }

    solution_instance = solution_class()  # Create one instance for all tests
    try:
        method_to_test = getattr(solution_instance, method_name)
    except AttributeError:
        print(
            f"{RED}Error: Could not access method '{method_name}' on an instance of '{solution_class.__name__}'.{RESET}"
        )
        return {
            "total_cases": len(test_cases),
            "passed": 0,
            "failed": len(test_cases),
            "errors": len(test_cases),
            "total_time_ms": 0.000,
        }

    passed_count = 0
    failed_count = 0
    error_count = 0
    total_time = 0.0

    print(f"{BLUE}Running tests for {solution_class.__name__}.{method_name}:{RESET}")
    print("-" * 70)

    for i, case_spec in enumerate(test_cases):
        case_name = case_spec.get("name", f"Test Case {i + 1}")

        # Prepare arguments
        args = case_spec.get("args", ())
        if not isinstance(args, tuple):
            # For convenience, if a single non-tuple arg is provided, wrap it.
            # However, it's best practice for users to provide a tuple e.g. (arg1,)
            print(
                f"{YELLOW}Warning for '{case_name}': 'args' should ideally be a tuple. "
                f"Attempting to treat {_format_value(args)} as a single argument tuple.{RESET}"
            )
            args = (args,)

        kwargs = case_spec.get("kwargs", {})
        expected_output = case_spec.get("expected")
        expected_exception_type = case_spec.get("expected_exception")
        comparator = case_spec.get("comparator")
        sort_output = case_spec.get("sort_output_before_compare", False)
        output_arg_idx = case_spec.get("output_arg_index")
        case_timeout = case_spec.get("timeout", default_timeout)
        setup_fn = case_spec.get("setup")
        teardown_fn = case_spec.get("teardown")

        # Make a copy of args if output_arg_idx is used, to avoid modification issues
        # if args itself is a tuple of mutable objects that we need to preserve for display.
        # The actual mutable objects *within* args will be passed by reference.
        current_args_for_call = list(
            args
        )  # Make list to allow modification if needed by output_arg_idx logic
        # This is primarily for the case where output_arg_idx is used.
        # The function will receive elements of this list.

        print(f"{MAGENTA}Running {case_name}...{RESET}")
        if args or kwargs:
            input_str_parts = []
            if args:
                input_str_parts.append(f"args: {_format_value(args)}")
            if kwargs:
                input_str_parts.append(f"kwargs: {_format_value(kwargs)}")
            print(f"  Input: {', '.join(input_str_parts)}")
        else:
            print("  Input: (No arguments)")

        start_time = time.perf_counter()

        timed_call = _TimedCall(
            method_to_test, tuple(current_args_for_call), kwargs, setup_fn, teardown_fn
        )
        actual_output, raised_exception, tb_str = timed_call.run(case_timeout)

        duration = (time.perf_counter() - start_time) * 1000  # milliseconds
        total_time += duration

        if output_arg_idx is not None:
            if raised_exception is None:  # Only fetch if no error during call
                try:
                    actual_output = current_args_for_call[output_arg_idx]
                    print(f"  {CYAN}Output from arg index {output_arg_idx}.{RESET}")
                except IndexError:
                    raised_exception = IndexError(
                        f"output_arg_index {output_arg_idx} is out of bounds for args of length {len(current_args_for_call)}."
                    )
                    tb_str = traceback.format_exc()

        # --- Test Outcome Evaluation ---
        if expected_exception_type:
            print(f"  Expected Exception: {expected_exception_type.__name__}")
            if raised_exception:
                if isinstance(raised_exception, expected_exception_type):
                    passed_count += 1
                    print(f"  {GREEN}PASSED! (Correct exception raised){RESET}")
                    print(
                        f"  Raised: {_format_value(type(raised_exception).__name__)}: {raised_exception}"
                    )
                else:
                    failed_count += 1
                    print(f"  {RED}FAILED! (Wrong exception raised){RESET}")
                    print(
                        f"  Expected Exception: {_format_value(expected_exception_type.__name__)}"
                    )
                    print(
                        f"  Actually Raised:    {_format_value(type(raised_exception).__name__)}: {raised_exception}"
                    )
                    if tb_str:
                        print(f"{YELLOW}{tb_str}{RESET}")
            else:
                failed_count += 1
                print(f"  {RED}FAILED! (Expected exception not raised){RESET}")
                print(
                    f"  Expected Exception: {_format_value(expected_exception_type.__name__)}"
                )
                print(f"  Actual Output: {_format_value(actual_output)}")
        elif raised_exception:
            error_count += 1
            print(f"  {RED}ERROR during execution!{RESET}")
            print(
                f"  Exception: {_format_value(type(raised_exception).__name__)}: {raised_exception}"
            )
            if tb_str:
                print(f"{YELLOW}{tb_str}{RESET}")
        else:  # No exception expected, no exception raised
            processed_actual = actual_output
            processed_expected = expected_output

            if sort_output:
                # Check if both are lists and sortable
                can_sort_actual = isinstance(actual_output, list)
                can_sort_expected = isinstance(expected_output, list)
                if can_sort_actual and can_sort_expected:
                    try:
                        processed_actual = sorted(list(actual_output))  # Sort a copy
                        processed_expected = sorted(
                            list(expected_output)
                        )  # Sort a copy
                        print(f"  {CYAN}Sorted list outputs for comparison.{RESET}")
                    except TypeError:
                        print(
                            f"  {YELLOW}Warning: Could not sort lists for comparison (mixed types). Comparing as is.{RESET}"
                        )
                elif (can_sort_actual or can_sort_expected) and (
                    actual_output is not None and expected_output is not None
                ):
                    print(
                        f"  {YELLOW}Warning: 'sort_output_before_compare' is True, but types mismatch for sorting. Comparing as is.{RESET}"
                    )

            match = False
            if comparator:
                print(f"  {CYAN}Using custom comparator.{RESET}")
                try:
                    # MODIFICATION: Pass current_args_for_call (state of args after function execution)
                    match = comparator(
                        processed_actual, processed_expected, current_args_for_call
                    )
                except Exception as e_comp:
                    error_count += 1
                    print(f"  {RED}ERROR in custom comparator!{RESET}")
                    print(f"{YELLOW}{traceback.format_exc()}{RESET}")
                    print(f"{RED}Comparator Error: {e_comp}{RESET}")
                    print("-" * 70)
                    continue
            else:
                match = processed_actual == processed_expected

            if match:
                passed_count += 1
                print(f"  {GREEN}PASSED!{RESET}")
                print(f"  Expected: {_format_value(expected_output)}")
                print(f"  Actual:   {_format_value(actual_output)}")
                if sort_output and processed_actual != actual_output:
                    print(
                        f"    (Sorted Actual for comparison: {_format_value(processed_actual)})"
                    )
                    print(
                        f"    (Sorted Expected for comparison: {_format_value(processed_expected)})"
                    )
            else:
                failed_count += 1
                print(f"  {RED}FAILED!{RESET}")
                print(f"  Expected: {_format_value(expected_output)}")
                print(f"  Actual:   {_format_value(actual_output)}")
                if (
                    sort_output
                    and isinstance(actual_output, list)
                    and isinstance(expected_output, list)
                ):
                    print(
                        f"    (Sorted Expected for comparison: {_format_value(processed_expected)})"
                    )
                    print(
                        f"    (Sorted Actual for comparison:   {_format_value(processed_actual)})"
                    )
                # Provide diff for complex types
                if isinstance(expected_output, (list, dict)) or isinstance(
                    actual_output, (list, dict)
                ):
                    diff_output = _get_diff(processed_expected, processed_actual)
                    if diff_output:  # Only print if there's a diff
                        print(f"  {CYAN}Difference:{RESET}\n{diff_output}")

        print(f"  Time: {duration:.3f} ms")
        print("-" * 70)

    # Summary
    print("\n" + "=" * 70)
    print(f"{BLUE}Test Suite Summary:{RESET}")
    print(f"  Total Tests: {len(test_cases)}")
    if passed_count > 0:
        print(f"  {GREEN}Passed: {passed_count}{RESET}")
    if failed_count > 0:
        print(f"  {RED}Failed: {failed_count}{RESET}")
    if error_count > 0:
        print(
            f"  {YELLOW}Errors: {error_count}{RESET}"
        )  # Includes timeouts, setup/teardown errors
    print(f"  Total Execution Time: {total_time:.3f} ms")
    print("=" * 70 + "\n")

    if failed_count == 0 and error_count == 0 and len(test_cases) > 0:
        print(f"{GREEN}All tests passed! Congratulations!{RESET}")
    elif len(test_cases) == 0:
        print(f"{YELLOW}No test cases provided.{RESET}")
    else:
        print(
            f"{RED}Some tests did not pass. Please review the failures/errors.{RESET}"
        )

    return {
        "total_cases": len(test_cases),
        "passed": passed_count,
        "failed": failed_count,
        "errors": error_count,
        "total_time_ms": total_time,
    }
