from typing import List, Dict, Any, Tuple

# Assume your solution file is: solutions/easy/remove_duplicates_sorted_array.py
# and it has: class Solution: def removeDuplicates(self, nums: List[int]) -> int:

METHOD_NAME = "removeDuplicates"


# You would need to define a Colors class or similar for console output if desired.
# Example:
class Colors:
    RED = "\033[91m"
    RESET = "\033[0m"


def remove_duplicates_comparator(
    actual_k: int,  # This is the 'k' returned by Solution.removeDuplicates
    expected_data: Dict[str, Any],  # This is the 'expected' dict from TEST_CASES
    all_args_after_call: Tuple[
        List[int], ...
    ],  # Tuple of args after Solution.removeDuplicates ran
    # For this problem, it's (modified_nums_list,)
) -> bool:
    """
    Custom comparator for the "Remove Duplicates from Sorted Array" problem.
    - actual_k: The integer k returned by the user's solution.
    - expected_data: A dictionary like {"k": expected_k_value, "nums_prefix": expected_nums_array}
    - all_args_after_call: A tuple containing the input arguments after the function call.
                           For removeDuplicates(nums), this will be (modified_nums_list,).
    """
    expected_k_value = expected_data.get("k")
    expected_nums_prefix = expected_data.get("nums_prefix")

    if actual_k != expected_k_value:
        print(f"  {Colors.RED}Comparator Detail: k mismatch.{Colors.RESET}")
        print(f"    Expected k: {expected_k_value}")
        print(f"    Actual k:   {actual_k}")
        return False

    # Get the modified nums list from the arguments passed to the solution
    # It's the first argument, so index 0.
    modified_nums_list = all_args_after_call[0]

    # Check if the length of the modified list is sufficient (it should be at least k)
    # (Though LeetCode doesn't strictly require trimming the list, only that first k are correct)
    # For robust testing, we ensure we can access up to k elements.
    if len(modified_nums_list) < actual_k:
        print(
            f"  {Colors.RED}Comparator Detail: Modified nums array is shorter than returned k.{Colors.RESET}"
        )
        print(f"    Returned k: {actual_k}")
        print(f"    Length of modified_nums: {len(modified_nums_list)}")
        return False

    # Check if the length of the expected prefix matches k
    if len(expected_nums_prefix) != actual_k:
        print(
            f"  {Colors.RED}Comparator Detail: Test case 'expected_nums_prefix' length ({len(expected_nums_prefix)}) "
            f"does not match returned/expected k ({actual_k}). Please check test case definition.{Colors.RESET}"
        )
        return False  # This indicates an issue with the test case itself

    # Compare the first k elements
    for i in range(actual_k):
        if modified_nums_list[i] != expected_nums_prefix[i]:
            print(
                f"  {Colors.RED}Comparator Detail: Mismatch in nums array at index {i}.{Colors.RESET}"
            )
            print(f"    Expected nums[{i}]: {expected_nums_prefix[i]}")
            print(f"    Actual nums[{i}]:   {modified_nums_list[i]}")
            print(f"    Full expected prefix: {expected_nums_prefix}")
            print(f"    Full actual nums[:k]: {modified_nums_list[:actual_k]}")
            return False

    return True


TEST_CASES: List[Dict[str, Any]] = [
    {
        "name": "LeetCode Example 1",
        "args": ([1, 1, 2],),  # nums is a list, passed as a single argument in a tuple
        "expected": {"k": 2, "nums_prefix": [1, 2]},
        "comparator": remove_duplicates_comparator,
    },
    {
        "name": "LeetCode Example 2",
        "args": ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4],),
        "expected": {"k": 5, "nums_prefix": [0, 1, 2, 3, 4]},
        "comparator": remove_duplicates_comparator,
    },
    {
        "name": "No duplicates",
        "args": ([1, 2, 3, 4, 5],),
        "expected": {"k": 5, "nums_prefix": [1, 2, 3, 4, 5]},
        "comparator": remove_duplicates_comparator,
    },
    {
        "name": "All duplicates",
        "args": ([1, 1, 1, 1],),
        "expected": {"k": 1, "nums_prefix": [1]},
        "comparator": remove_duplicates_comparator,
    },
    {
        "name": "Empty array",
        "args": ([],),
        "expected": {"k": 0, "nums_prefix": []},
        "comparator": remove_duplicates_comparator,
    },
    {
        "name": "Single element",
        "args": ([7],),
        "expected": {"k": 1, "nums_prefix": [7]},
        "comparator": remove_duplicates_comparator,
    },
    {
        "name": "Two distinct elements",
        "args": ([1, 2],),
        "expected": {"k": 2, "nums_prefix": [1, 2]},
        "comparator": remove_duplicates_comparator,
    },
    {
        "name": "Two duplicate elements",
        "args": ([5, 5],),
        "expected": {"k": 1, "nums_prefix": [5]},
        "comparator": remove_duplicates_comparator,
    },
    {
        "name": "Three elements, two duplicates",
        "args": ([1, 2, 2],),
        "expected": {"k": 2, "nums_prefix": [1, 2]},
        "comparator": remove_duplicates_comparator,
    },
    {
        "name": "Three elements, first two duplicates",
        "args": ([1, 1, 2],),
        "expected": {"k": 2, "nums_prefix": [1, 2]},
        "comparator": remove_duplicates_comparator,
    },
    {
        "name": "Alternating duplicates",
        "args": ([1, 1, 2, 2, 3, 3],),
        "expected": {"k": 3, "nums_prefix": [1, 2, 3]},
        "comparator": remove_duplicates_comparator,
    },
    {
        "name": "Longer array with various duplicates",
        "args": ([-3, -1, -1, 0, 0, 0, 1, 1, 2, 3, 3, 3, 3, 4, 5, 5, 6],),
        "expected": {"k": 9, "nums_prefix": [-3, -1, 0, 1, 2, 3, 4, 5, 6]},
        "comparator": remove_duplicates_comparator,
    },
    {
        "name": "All negative numbers with duplicates",
        "args": ([-5, -5, -4, -3, -3, -3, -1, -1],),
        "expected": {"k": 4, "nums_prefix": [-5, -4, -3, -1]},
        "comparator": remove_duplicates_comparator,
    },
    {
        "name": "Array with zero and duplicates",
        "args": ([-1, 0, 0, 0, 1, 1],),
        "expected": {"k": 3, "nums_prefix": [-1, 0, 1]},
        "comparator": remove_duplicates_comparator,
    },
    {
        "name": "Larger values",
        "args": ([100, 100, 150, 200, 200, 200, 250],),
        "expected": {"k": 4, "nums_prefix": [100, 150, 200, 250]},
        "comparator": remove_duplicates_comparator,
    },
]

# Optional: You can also define a default timeout for this specific problem's tests
# DEFAULT_TIMEOUT = 1.0  # seconds
