# LeetCode Test Suite: Test Definition File Conventions

This document outlines the conventions for creating test definition files used by the `run_tests.py` script and the `framework.py` testing engine.

## File Location and Naming

- Test definition files are located in the `test_definitions/` directory, mirrored to the `solutions/` directory structure.
- For a solution file at `solutions/<difficulty>/<problem_file_stem>.py` (e.g., `solutions/easy/0001_two_sum.py`), the corresponding test definition file **must** be at `test_definitions/<difficulty>/<problem_file_stem>.py` (e.g., `test_definitions/easy/0001_two_sum.py`).
- The `<problem_file_stem>` is the name of the solution Python file without the `.py` extension. It can include a LeetCode number prefix (e.g., `0001_two_sum`) or be just the name (e.g., `two_sum`).

## File Contents

Each test definition Python file must define at least two top-level variables:

1.  `METHOD_NAME` (str): The exact name of the method within the `Solution` class (defined in the corresponding solution file) that should be tested.
2.  `TEST_CASES` (List[Dict[str, Any]]): A list where each element is a dictionary representing a single test case.

Optionally, you can also define:

3.  `DEFAULT_TIMEOUT` (float, optional): A default timeout in seconds for each test case in this file. This can be overridden by a `timeout` key within an individual test case dictionary.

## Test Case Dictionary Structure

Each dictionary within the `TEST_CASES` list defines a single test and can contain the following keys:

### Required Keys:

- **`args`** (Tuple):

  - A tuple containing the positional arguments to be passed to the solution method.
  - If the method takes one argument `arg1`, `args` should be `(arg1,)`. (Note the trailing comma for a single-element tuple).
  - If the method takes multiple arguments `arg1, arg2`, `args` should be `(arg1, arg2)`.
  - If the method takes no arguments, `args` should be `()`.
  - **Example:** `("args": ([1, 2, 3], 6),)` for a method `myMethod(self, nums_list, target_sum)`

- **`expected`** (Any):
  - The expected output from the solution method.
  - This value is directly compared with the actual return value of the solution method, unless a `comparator` is provided or `expected_exception` is used.
  - For problems with complex validation (e.g., in-place modifications + return value), this field can be a dictionary or custom object that your `comparator` function understands.
  - **Example:** `"expected": [0, 1]` or `"expected": {"k": 2, "nums_prefix": [1, 2]}` (if used with a custom comparator).

### Optional Keys:

- **`name`** (str, optional):

  - A descriptive name for the test case. If not provided, a default name like "Test Case X" will be used.
  - **Example:** `"name": "Example 1: Basic case"`

- **`kwargs`** (Dict[str, Any], optional):

  - A dictionary of keyword arguments to be passed to the solution method.
  - Defaults to an empty dictionary `{}` if not provided.
  - **Example:** `"kwargs": {"operation": "add"}` for a method `myMethod(self, x, operation="default_op")`

- **`expected_exception`** (Type[BaseException], optional):

  - If the test case is expected to raise a specific exception, set this key to the exception type (e.g., `ValueError`, `TypeError`).
  - If this key is present, the `expected` key is ignored. The test passes if the specified exception (or a subclass of it) is raised.
  - **Example:** `"expected_exception": ValueError`

- **`comparator`** (Callable[[Any, Any, Tuple], bool], optional):

  - A custom function used to compare the actual output with the expected output.
  - **Signature:** `my_comparator(actual_output, expected_value, all_args_after_call) -> bool`
    - `actual_output`: The direct return value from the solution method (unless `output_arg_index` is used, in which case it's the value of that argument).
    - `expected_value`: The value provided in the `expected` key of the test case dictionary.
    - `all_args_after_call`: A tuple containing all positional arguments as they exist _after_ the solution method has executed. This is crucial for verifying in-place modifications. For a method `myMethod(self, arg1, arg2)`, this tuple would be `(modified_arg1, modified_arg2)`.
  - The comparator function should return `True` if the actual outcome matches the expected outcome according to its logic, and `False` otherwise.
  - It's good practice for the comparator to print detailed diagnostic messages if the comparison fails.
  - **Example:** `"comparator": float_comparator_with_tolerance` (where `float_comparator_with_tolerance` is a defined function).

- **`sort_output_before_compare`** (bool, optional):

  - If `True`, and if both the actual output and the expected output are lists, they will be sorted (as copies) before comparison.
  - Useful for problems where the order of elements in a list output does not matter.
  - Defaults to `False`. This key is ignored if a `comparator` is provided.
  - **Example:** `"sort_output_before_compare": True`

- **`output_arg_index`** (int, optional):

  - Specifies the index of a positional argument (from `args`) whose state _after_ the function call should be considered the "actual output" for comparison.
  - This is useful for functions that modify an argument in-place and return `None` (or something else), but you want to test the state of the modified argument directly against `expected`.
  - If used, the value of `args[output_arg_index]` after the function call becomes the `actual_output` passed to the standard comparison logic or to the `comparator`.
  - **Example:** `"output_arg_index": 0` (to test the state of the first argument).

- **`timeout`** (float, optional):

  - The maximum execution time in seconds for this specific test case.
  - Overrides the `DEFAULT_TIMEOUT` defined at the file level, or the global default if neither is set.
  - If execution exceeds this time, the test is marked as an "ERROR" with a `TimeoutError`.
  - **Example:** `"timeout": 0.5` (for 0.5 seconds).

- **`setup`** (Callable[[], None], optional):

  - A function to be called immediately before this specific test case runs. It takes no arguments and should return `None`.
  - Useful for setting up global state or resources specific to a test.
  - **Example:** `"setup": my_test_setup_function`

- **`teardown`** (Callable[[], None], optional):
  - A function to be called immediately after this specific test case finishes (regardless of whether it passed, failed, or errored, but after the solution method and before the next test case's setup). It takes no arguments and should return `None`.
  - Useful for cleaning up resources set up by the `setup` function.
  - **Example:** `"teardown": my_test_teardown_function`

## Necessary Imports

Within your test definition file, you will typically need:

- `from typing import List, Dict, Any, Tuple, Optional, Callable, Type` (or specific types as needed for your test case data and function signatures).
- If using custom data structures like `ListNode` or `TreeNode` provided by the framework, or helper functions to create them:
  ```python
  from framework import ListNode, TreeNode, list_to_linkedlist, list_to_treenode
  ```
- If defining `expected_exception`, you might need to import specific exception types if they are not built-in (e.g., `from my_custom_exceptions import MyError`).
- Any other modules required by your custom comparator functions or setup/teardown functions.

## Data Structure Helpers

The framework provides helpers for common LeetCode data structures, accessible via `from framework import ...`:

- **`ListNode`**: Class for linked list nodes. Implements `__eq__` for value-based list comparison and `__repr__` for display.
- **`TreeNode`**: Class for binary tree nodes. Implements `__eq__` for value-based tree comparison (recursive) and `__repr__` for display.
- **`list_to_linkedlist(items: List[Any]) -> Optional[ListNode]`**: Converts a Python list into a linked list of `ListNode` objects.
- **`list_to_treenode(items: List[Optional[int]]) -> Optional[TreeNode]`**: Converts a Python list (representing a level-order binary tree with `None` for null nodes, similar to LeetCode's representation) into a tree of `TreeNode` objects.
- `pretty_print_linked_list(head: Optional[ListNode]):`: Prints the elements of a linked list in a readable format, starting from the given `head` node.
- `pretty_print_tree(node: Optional[TreeNode], prefix: str = "", is_left bool = True):`: Prints the structure of a binary tree in a visually organized way, starting from the given `root` node.
  - prefix: The string used for indentation, as determined by the value of is_left and the current tree structure.
  - is_left: A boolean indicating if the current node is a left child, which affects how prefix is constructed.
    **Usage Example for Data Structures:**

```python
from framework import list_to_linkedlist, list_to_treenode

# ...
TEST_CASES = [
    {
        "name": "Linked List Example",
        "args": (list_to_linkedlist([1, 2, 3]),),
        "expected": list_to_linkedlist([1, 2, 3]) # Or some transformed list
    },
    {
        "name": "Binary Tree Example",
        "args": (list_to_treenode([1, None, 2, 3]),),
        "expected": True # e.g., if the method checks a property of the tree
    }
]
```

## Creating and Using a Custom Comparator

A custom comparator is a powerful tool for tests where simple equality (`==`) is insufficient or when multiple aspects of the outcome need to be verified (e.g., a return value AND an in-place modification).

1.  **Define the Comparator Function:**
    The function must accept three arguments:

    - `actual_output`: The value returned by the solution method (or the value of the argument at `output_arg_index` if specified).
    - `expected_value`: The content of the `expected` key from your test case dictionary.
    - `all_args_after_call`: A tuple of all positional arguments passed to the solution method, reflecting their state _after_ the solution method has executed.

    The function should return `True` if the test passes according to its logic, `False` otherwise.

    ```python
    # Example: Comparator for a problem that returns a count and modifies an input list
    # (like "Remove Duplicates from Sorted Array")

    # If you need colors for print statements within the comparator:
    # from framework import Colors # Or define a minimal local Colors class
    class LocalColors:
        RED = "\033[91m"; RESET = "\033[0m" # etc.

    def my_complex_comparator(actual_k: int, expected_dict: Dict[str, Any], args_after: Tuple) -> bool:
        expected_k = expected_dict.get("k")
        expected_nums_prefix = expected_dict.get("nums_prefix")
        modified_nums_list = args_after[0] # Assuming 'nums' was the first argument

        if actual_k != expected_k:
            print(f"  {LocalColors.RED}Comparator: k mismatch. Expected {expected_k}, got {actual_k}{LocalColors.RESET}")
            return False

        if len(modified_nums_list) < actual_k:
            print(f"  {LocalColors.RED}Comparator: Modified nums too short.{LocalColors.RESET}")
            return False # Or handle as per problem spec

        for i in range(actual_k):
            if modified_nums_list[i] != expected_nums_prefix[i]:
                print(f"  {LocalColors.RED}Comparator: Nums prefix mismatch at index {i}. "
                      f"Expected {expected_nums_prefix[i]}, got {modified_nums_list[i]}{LocalColors.RESET}")
                return False
        return True
    ```

2.  **Assign to Test Case:**
    In your `TEST_CASES` list, for the relevant test case dictionary, set the `comparator` key to your defined function:
    ```python
    TEST_CASES = [
        {
            "name": "In-place modification test",
            "args": ([1, 1, 2, 2, 3],),
            "expected": {"k": 3, "nums_prefix": [1, 2, 3]},
            "comparator": my_complex_comparator
        }
    ]
    ```

**Important Notes for Comparators:**

- The `expected` field in your test case can be structured in any way that your comparator function understands (e.g., a dictionary, a tuple of multiple expected values).
- Printing informative messages from within the comparator upon failure is highly recommended for debugging.
- The `all_args_after_call` tuple provides read-only access to the state of the arguments. If you need to modify them further for comparison purposes (e.g., sorting a copy), ensure you work with copies to avoid unintended side effects.

## Example Test Definition File (`test_definitions/easy/0001_two_sum.py`)

```python
from typing import List, Dict, Any, Tuple # Standard type hints

# METHOD_NAME is required
METHOD_NAME = "twoSum"

# TEST_CASES is required
TEST_CASES: List[Dict[str, Any]] = [
    {
        "name": "Example 1",
        "args": ([2, 7, 11, 15], 9), # args is a tuple: (nums_list, target_int)
        "expected": [0, 1]          # expected is a list of integers
    },
    {
        "name": "Example 2 with sort_output",
        "args": ([3, 2, 4], 6),
        "expected": [1, 2], # Solution might return [2,1] or [1,2]
        "sort_output_before_compare": True # Sorts both actual and expected lists before comparing
    },
    {
        "name": "Test with kwargs (if method supported them)",
        "args": ([3,3],), # Assuming target is a kwarg
        "kwargs": {"target": 6},
        "expected": [0,1]
    },
    {
        "name": "Test expecting an exception (e.g., if input constraints were violated)",
        # "args": (None, 0), # Example of invalid input
        # "expected_exception": TypeError # If the method is expected to raise TypeError
        # "expected": None # This would be ignored if expected_exception is present
    }
]

# DEFAULT_TIMEOUT is optional
# DEFAULT_TIMEOUT = 1.0 # Set a 1-second default timeout for all tests in this file
```

By adhering to these conventions, you can create clear, maintainable, and comprehensive test definitions for your LeetCode solutions, leveraging the full power of the testing framework.
