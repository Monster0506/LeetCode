# leet_code_project/run_tests.py
import sys
import importlib
import argparse
import traceback
from pathlib import Path
import re  # For parsing filenames and ranges

from typing import Optional

# --- Path Setup: Add project root to sys.path ---
PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
# --- End Path Setup ---

try:
    from framework import run_leetcode_tests  # This now returns a summary dict
except ImportError:
    print("Error: Could not import 'run_leetcode_tests' from framework.")
    print("Ensure framework/framework.py and framework/__init__.py exist and")
    print(f"PROJECT_ROOT ({PROJECT_ROOT}) is correctly added to sys.path.")
    sys.exit(1)

SOLUTIONS_DIR = PROJECT_ROOT / "solutions"
TEST_DEFS_DIR = PROJECT_ROOT / "test_definitions"


# Simple color class for console output
class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    RESET = "\033[0m"


def parse_problem_filename(filename_stem: str) -> tuple[Optional[str], str]:
    match = re.match(r"^(\d{1,4})_(.+)$", filename_stem)
    if match:
        number = match.group(1).zfill(4)
        name = match.group(2)
        return number, name
    return None, filename_stem


def parse_range_spec(spec: str) -> Optional[tuple[Optional[int], Optional[int]]]:
    """
    Parses a range string like "1-10", "5-", "-20".
    Returns (start, end) or None if not a range.
    None for start/end means unbounded in that direction.
    """
    if "-" not in spec:
        return None

    parts = spec.split("-", 1)
    start_str, end_str = parts[0], parts[1]

    start: Optional[int] = None
    end: Optional[int] = None

    if start_str:
        if not start_str.isdigit():
            return None  # Invalid start
        start = int(start_str)

    if end_str:
        if not end_str.isdigit():
            return None  # Invalid end
        end = int(end_str)

    if start is None and end is None and spec != "-":  # Avoid matching just "-"
        return None

    return start, end


def discover_and_run_tests(target_spec: str):
    overall_summary = {
        "problems_attempted": 0,
        "problems_fully_passed": 0,
        "problems_with_issues": 0,
        "total_test_cases_run": 0,
        "total_test_cases_passed": 0,
        "total_test_cases_failed": 0,
        "total_test_cases_errored": 0,
        "failed_problem_details": [],  # List of dicts {id: str, summary: dict}
    }

    # Step 1: Collect all potential problems
    all_problem_infos = []
    for diff_dir in SOLUTIONS_DIR.iterdir():
        if diff_dir.is_dir() and not diff_dir.name.startswith(("_", ".")):
            difficulty = diff_dir.name
            for sol_file in diff_dir.glob("*.py"):
                if (
                    sol_file.name.startswith(("_", "."))
                    or sol_file.name == "__init__.py"
                ):
                    continue

                file_stem = sol_file.stem
                problem_number, base_name = parse_problem_filename(file_stem)

                solution_module_path = f"solutions.{difficulty}.{file_stem}"
                # MODIFIED: Test config file has same stem as solution file
                test_config_module_path = f"test_definitions.{difficulty}.{file_stem}"
                problem_id_display = f"{difficulty}/{file_stem}"
                expected_config_file = (
                    TEST_DEFS_DIR / difficulty / f"{file_stem}.py"  # MODIFIED
                )

                all_problem_infos.append(
                    {
                        "difficulty": difficulty,
                        "file_stem": file_stem,
                        "problem_number": problem_number,  # String or None
                        "base_name": base_name,
                        "solution_module_path": solution_module_path,
                        "test_config_module_path": test_config_module_path,
                        "problem_id_display": problem_id_display,
                        "solution_file_exists": sol_file.exists(),
                        "config_file_exists": expected_config_file.exists(),
                    }
                )

    # Step 2: Filter problems based on target_spec
    filtered_problems = []
    parsed_range = parse_range_spec(target_spec)

    if parsed_range:
        range_start, range_end = parsed_range
        for p_info in all_problem_infos:
            if p_info["problem_number"]:
                try:
                    num = int(p_info["problem_number"])
                    in_range = True
                    if range_start is not None and num < range_start:
                        in_range = False
                    if range_end is not None and num > range_end:
                        in_range = False
                    if in_range:
                        filtered_problems.append(p_info)
                except ValueError:
                    continue  # Should not happen if problem_number is from parse_problem_filename
    elif target_spec.isdigit():
        normalized_target_number = target_spec.zfill(4)
        for p_info in all_problem_infos:
            if p_info["problem_number"] == normalized_target_number:
                filtered_problems.append(p_info)
    elif target_spec == "all":
        filtered_problems = all_problem_infos
    elif target_spec in ["easy", "medium", "hard"]:
        for p_info in all_problem_infos:
            if p_info["difficulty"] == target_spec:
                filtered_problems.append(p_info)
    elif "/" in target_spec:
        target_difficulty, target_name_or_num_part = target_spec.split("/", 1)
        for p_info in all_problem_infos:
            if p_info["difficulty"] == target_difficulty:
                if target_name_or_num_part.isdigit():
                    normalized_num_part = target_name_or_num_part.zfill(4)
                    if p_info["problem_number"] == normalized_num_part:
                        filtered_problems.append(p_info)
                else:
                    if (
                        p_info["file_stem"] == target_name_or_num_part
                        or p_info["base_name"] == target_name_or_num_part
                    ):
                        filtered_problems.append(p_info)
    else:
        for p_info in all_problem_infos:
            if p_info["file_stem"] == target_spec or p_info["base_name"] == target_spec:
                filtered_problems.append(p_info)

    if not filtered_problems:
        print(
            f"{Colors.YELLOW}No problems found matching spec: '{target_spec}'{Colors.RESET}"
        )
        return

    # Step 3: Run tests for filtered problems
    for p_info in filtered_problems:
        if not p_info["solution_file_exists"]:
            print(
                f"{Colors.YELLOW}Skipping {p_info['problem_id_display']}: Solution file not found.{Colors.RESET}"
            )
            continue
        if not p_info["config_file_exists"]:
            print(
                f"{Colors.YELLOW}Skipping {p_info['problem_id_display']}: Test definition file not found ({TEST_DEFS_DIR / p_info['difficulty'] / (p_info['file_stem'] + '.py')}).{Colors.RESET}"
            )
            continue

        print(
            f"\n{Colors.BLUE}{'='*15} Running tests for: {p_info['problem_id_display']} {'='*15}{Colors.RESET}"
        )
        overall_summary["problems_attempted"] += 1
        try:
            solution_module = importlib.import_module(p_info["solution_module_path"])
            test_config_module = importlib.import_module(
                p_info["test_config_module_path"]
            )

            solution_class = getattr(solution_module, "Solution", None)
            if not solution_class:
                print(
                    f"{Colors.RED}Error: 'Solution' class not found in {p_info['solution_module_path']}.py{Colors.RESET}"
                )
                overall_summary["problems_with_issues"] += 1
                overall_summary["failed_problem_details"].append(
                    {
                        "id": p_info["problem_id_display"],
                        "reason": "Solution class not found",
                        "summary": None,
                    }
                )
                continue

            method_name = getattr(test_config_module, "METHOD_NAME", None)
            test_cases = getattr(test_config_module, "TEST_CASES", None)
            default_timeout = getattr(test_config_module, "DEFAULT_TIMEOUT", None)

            if method_name is None or test_cases is None:
                print(
                    f"{Colors.RED}Error: METHOD_NAME or TEST_CASES not defined in {p_info['test_config_module_path']}.py{Colors.RESET}"
                )
                overall_summary["problems_with_issues"] += 1
                overall_summary["failed_problem_details"].append(
                    {
                        "id": p_info["problem_id_display"],
                        "reason": "METHOD_NAME or TEST_CASES missing",
                        "summary": None,
                    }
                )
                continue

            if not test_cases:  # Empty list of test cases
                print(
                    f"{Colors.YELLOW}Warning: No test cases defined for {p_info['problem_id_display']}. Skipping execution for this problem.{Colors.RESET}"
                )
                # Not necessarily an "issue" for the overall summary unless we want to count it.
                # For now, it just means no tests run for this problem.
                # We could add a category for "problems_with_no_tests".
                continue

            problem_run_summary = run_leetcode_tests(
                solution_class=solution_class,
                method_name=method_name,
                test_cases=test_cases,
                default_timeout=default_timeout,
            )

            overall_summary["total_test_cases_run"] += problem_run_summary[
                "total_cases"
            ]
            overall_summary["total_test_cases_passed"] += problem_run_summary["passed"]
            overall_summary["total_test_cases_failed"] += problem_run_summary["failed"]
            overall_summary["total_test_cases_errored"] += problem_run_summary["errors"]

            if (
                problem_run_summary["failed"] == 0
                and problem_run_summary["errors"] == 0
                and problem_run_summary["total_cases"] > 0
            ):
                overall_summary["problems_fully_passed"] += 1
            elif (
                problem_run_summary["total_cases"] > 0
            ):  # Only count as issue if tests were run
                overall_summary["problems_with_issues"] += 1
                overall_summary["failed_problem_details"].append(
                    {
                        "id": p_info["problem_id_display"],
                        "reason": "Test case failures/errors",
                        "summary": problem_run_summary,
                    }
                )

        except ImportError as e:
            print(
                f"{Colors.RED}Error importing modules for {p_info['problem_id_display']}:{Colors.RESET}\n  {e}"
            )
            overall_summary["problems_with_issues"] += 1
            overall_summary["failed_problem_details"].append(
                {
                    "id": p_info["problem_id_display"],
                    "reason": f"ImportError: {e}",
                    "summary": None,
                }
            )
        except Exception as e:
            print(
                f"{Colors.RED}An unexpected error occurred for {p_info['problem_id_display']}:{Colors.RESET}\n  {e}"
            )
            traceback.print_exc()
            overall_summary["problems_with_issues"] += 1
            overall_summary["failed_problem_details"].append(
                {
                    "id": p_info["problem_id_display"],
                    "reason": f"Unexpected error: {e}",
                    "summary": None,
                }
            )
        # Individual problem summary is printed by run_leetcode_tests
        # print(f"{Colors.BLUE}{'-'*60}{Colors.RESET}") # Separator after each problem's detailed output

    # Print Overall Summary
    print(f"\n{Colors.MAGENTA}{'='*20} OVERALL TEST SUMMARY {'='*20}{Colors.RESET}")
    print(f"  Problems Attempted: {overall_summary['problems_attempted']}")
    if overall_summary["problems_attempted"] > 0:
        print(
            f"  {Colors.GREEN}Problems Fully Passed: {overall_summary['problems_fully_passed']}{Colors.RESET}"
        )
        if overall_summary["problems_with_issues"] > 0:
            print(
                f"  {Colors.RED}Problems with Issues: {overall_summary['problems_with_issues']}{Colors.RESET}"
            )

        print(f"\n  Total Test Cases Run:    {overall_summary['total_test_cases_run']}")
        if overall_summary["total_test_cases_run"] > 0:
            print(
                f"    {Colors.GREEN}Passed: {overall_summary['total_test_cases_passed']}{Colors.RESET}"
            )
            if overall_summary["total_test_cases_failed"] > 0:
                print(
                    f"    {Colors.RED}Failed: {overall_summary['total_test_cases_failed']}{Colors.RESET}"
                )
            if overall_summary["total_test_cases_errored"] > 0:
                print(
                    f"    {Colors.YELLOW}Errored: {overall_summary['total_test_cases_errored']}{Colors.RESET}"
                )

        if overall_summary["failed_problem_details"]:
            print(f"\n  {Colors.CYAN}Details for Problems with Issues:{Colors.RESET}")
            for issue in overall_summary["failed_problem_details"]:
                print(
                    f"    - {Colors.YELLOW}{issue['id']}{Colors.RESET}: {issue['reason']}"
                )
                if issue["summary"] and (
                    issue["summary"]["failed"] > 0 or issue["summary"]["errors"] > 0
                ):
                    summary = issue["summary"]
                    counts = []
                    if summary["failed"] > 0:
                        counts.append(f"{summary['failed']} failed")
                    if summary["errors"] > 0:
                        counts.append(f"{summary['errors']} errored")
                    if counts:
                        print(
                            f"      ({', '.join(counts)} out of {summary['total_cases']} test cases)"
                        )
    else:
        print(
            f"  {Colors.YELLOW}No problems were run based on the target spec '{target_spec}'.{Colors.RESET}"
        )
    print(
        f"{Colors.MAGENTA}{'='* (40 + len(' OVERALL TEST SUMMARY '))}{Colors.RESET}\n"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run LeetCode tests.",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=f"""
Examples:
  python run_tests.py all
  python run_tests.py easy
  python run_tests.py 0001                 (runs problem number 1, e.g., 0001_twosum.py)
  python run_tests.py 1-10                 (runs problems 1 through 10)
  python run_tests.py 5-                   (runs problems 5 and higher)
  python run_tests.py -20                  (runs problems up to 20)
  python run_tests.py easy/twosum
  python run_tests.py easy/0001_twosum
  python run_tests.py easy/1               (runs problem 1 from easy difficulty)
  python run_tests.py twosum               (searches for 'twosum' or 'XXXX_twosum')
  python run_tests.py 0001_twosum          (searches for '0001_twosum')

Test definition files should be in: {Colors.CYAN}{TEST_DEFS_DIR}/<difficulty>/<problem_file_stem>.py{Colors.RESET}
Solution files should be in:      {Colors.CYAN}{SOLUTIONS_DIR}/<difficulty>/<problem_file_stem>.py{Colors.RESET}
""",
    )
    parser.add_argument(
        "target",
        help="Target to test: 'all', difficulty, problem number (e.g., '1'), range (e.g., '1-10'), 'difficulty/name', 'difficulty/number', or 'problem_name'.",
    )
    args = parser.parse_args()

    discover_and_run_tests(args.target.strip())
