from typing import List, Dict, Any, Tuple
from framework import (
    Colors,
)


# METHOD_NAME is required
METHOD_NAME = "removeElement"


# Custom comparator function to check both the returned k and the modified nums array
def remove_element_comparator(
    actual_k: int, expected_dict: Dict[str, Any], args_after: Tuple
) -> bool:
    expected_k = expected_dict.get("k")
    expected_nums_prefix = expected_dict.get("nums_prefix")
    modified_nums_list = args_after[0]  # Assuming 'nums' is the first argument

    # Check if the returned k matches the expected k
    if actual_k != expected_k:
        print(
            f"  {Colors.RED}Comparator: Returned k mismatch. Expected {expected_k}, got {actual_k}{Colors.RESET}"
        )
        return False

    # Check if the modified nums list has at least k elements
    if len(modified_nums_list) < actual_k:
        print(
            f"  {Colors.RED}Comparator: Modified nums list is shorter than k.{Colors.RESET}"
        )
        # This case is unlikely if k is calculated correctly, but good for robustness
        return False

    # Sort the first k elements of the modified nums list and the expected prefix
    # Create copies to avoid modifying the original lists
    sorted_actual_prefix = sorted(modified_nums_list[:actual_k])
    sorted_expected_prefix = sorted(expected_nums_prefix)

    # Compare the sorted prefixes
    if sorted_actual_prefix != sorted_expected_prefix:
        print(
            f"  {Colors.RED}Comparator: Mismatch in the first k elements after sorting.{Colors.RESET}"
        )
        print(f"    Actual first k elements (sorted): {sorted_actual_prefix}")
        print(
            f"    Expected first k elements (sorted): {sorted_expected_prefix}{Colors.RESET}"
        )
        return False

    print(
        f"  {Colors.GREEN}Comparator: k and the first k elements match.{Colors.RESET}"
    )
    return True


# TEST_CASES is required
TEST_CASES: List[Dict[str, Any]] = [
    {
        "name": "Example 1",
        "args": ([3, 2, 2, 3], 3),  # nums, val
        "expected": {
            "k": 2,
            "nums_prefix": [2, 2],
        },  # Expected k and the elements that should be in the first k positions
        "comparator": remove_element_comparator,  # Use the custom comparator
    },
    {
        "name": "Example 2",
        "args": ([0, 1, 2, 2, 3, 0, 4, 2], 2),
        "expected": {"k": 5, "nums_prefix": [0, 1, 4, 0, 3]},
        "comparator": remove_element_comparator,
    },
    {
        "name": "No elements to remove",
        "args": ([1, 2, 3, 4, 5], 6),
        "expected": {"k": 5, "nums_prefix": [1, 2, 3, 4, 5]},
        "comparator": remove_element_comparator,
    },
    {
        "name": "All elements to remove",
        "args": ([1, 1, 1, 1], 1),
        "expected": {"k": 0, "nums_prefix": []},
        "comparator": remove_element_comparator,
    },
    {
        "name": "Empty array",
        "args": ([], 5),
        "expected": {"k": 0, "nums_prefix": []},
        "comparator": remove_element_comparator,
    },
    {
        "name": "Single element, removed",
        "args": ([7], 7),
        "expected": {"k": 0, "nums_prefix": []},
        "comparator": remove_element_comparator,
    },
    {
        "name": "Single element, not removed",
        "args": ([7], 5),
        "expected": {"k": 1, "nums_prefix": [7]},
        "comparator": remove_element_comparator,
    },
    {
        "name": "Array with duplicates, some removed",
        "args": ([1, 2, 3, 2, 4, 2], 2),
        "expected": {"k": 3, "nums_prefix": [1, 3, 4]},
        "comparator": remove_element_comparator,
    },
    {
        "name": "Large array, mixed values",
        "args": ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5], 2),
        "expected": {"k": 13, "nums_prefix": [1, 3, 4, 5, 6, 7, 8, 9, 0, 1, 3, 4, 5]},
        "comparator": remove_element_comparator,
    },
]

# DEFAULT_TIMEOUT = 1.0 # Set a 1-second default timeout for all tests in this file
