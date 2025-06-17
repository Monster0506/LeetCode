from typing import List, Dict, Any, Tuple

METHOD_NAME = "merge"


# Custom comparator function for in-place modification
def merge_comparator(
    actual_return_value: None, expected_nums1: List[int], all_args_after_call: Tuple
) -> bool:
    """
    Compares the state of nums1 after the merge operation.

    Args:
        actual_return_value: The return value of the merge method (expected to be None).
        expected_nums1: The expected final state of nums1.
        all_args_after_call: A tuple containing the arguments after the method call.
                             args_after[0] will be the modified nums1 list.
    Returns:
        True if the modified nums1 matches expected_nums1, False otherwise.
    """
    modified_nums1 = all_args_after_call[0]

    # First, verify the return value is None as specified by the problem.
    if actual_return_value is not None:
        print(f"  Comparator: Method returned {actual_return_value}, expected None.")
        return False

    # Now, compare the modified nums1 with the expected nums1
    if modified_nums1 != expected_nums1:
        print(
            f"  Comparator: Mismatch in nums1 after merge."
            f"\n    Expected: {expected_nums1}"
            f"\n    Actual:   {modified_nums1}"
        )
        return False

    return True


TEST_CASES: List[Dict[str, Any]] = [
    {
        "name": "Example 1: Standard merge",
        "args": ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3),
        "expected": [1, 2, 2, 3, 5, 6],
        "comparator": merge_comparator,
    },
    {
        "name": "Example 2: Empty nums2",
        "args": ([1], 1, [], 0),
        "expected": [1],
        "comparator": merge_comparator,
    },
    {
        "name": "Example 3: Empty nums1",
        "args": ([0], 0, [1], 1),
        "expected": [1],
        "comparator": merge_comparator,
    },
    {
        "name": "nums1 larger, no nums2 elements to insert",
        "args": ([4, 5, 6, 0, 0, 0], 3, [], 0),
        "expected": [4, 5, 6, 0, 0, 0],  # Nums1 should remain unchanged
        "comparator": merge_comparator,
    },
    {
        "name": "nums1 all zeros (empty initial m), nums2 elements",
        "args": ([0, 0, 0, 0, 0], 0, [1, 2, 3, 4, 5], 5),
        "expected": [1, 2, 3, 4, 5],
        "comparator": merge_comparator,
    },
    {
        "name": "nums1 with one element (m=1), nums2 has elements",
        "args": ([4, 0, 0], 1, [1, 2], 2),
        "expected": [1, 2, 4],
        "comparator": merge_comparator,
    },
    {
        "name": "nums2 with one element (n=1), nums1 has elements",
        "args": ([1, 2, 3, 0], 3, [4], 1),
        "expected": [1, 2, 3, 4],
        "comparator": merge_comparator,
    },
    {
        "name": "nums2 elements entirely smaller than nums1",
        "args": ([7, 8, 9, 0, 0, 0], 3, [1, 2, 3], 3),
        "expected": [1, 2, 3, 7, 8, 9],
        "comparator": merge_comparator,
    },
    {
        "name": "nums2 elements entirely larger than nums1",
        "args": ([1, 2, 3, 0, 0, 0], 3, [7, 8, 9], 3),
        "expected": [1, 2, 3, 7, 8, 9],
        "comparator": merge_comparator,
    },
    {
        "name": "Overlapping values, complex merge",
        "args": ([1, 3, 5, 0, 0, 0, 0], 3, [2, 4, 6, 8], 4),
        "expected": [1, 2, 3, 4, 5, 6, 8],
        "comparator": merge_comparator,
    },
    {
        "name": "Duplicate values across arrays",
        "args": ([1, 2, 3, 0, 0], 3, [2, 3], 2),
        "expected": [1, 2, 2, 3, 3],
        "comparator": merge_comparator,
    },
    {
        "name": "All elements in nums2 are duplicates of nums1 elements",
        "args": ([1, 2, 3, 0, 0], 3, [1, 2], 2),
        "expected": [1, 1, 2, 2, 3],
        "comparator": merge_comparator,
    },
    {
        "name": "Large number of elements (near constraint max)",
        "args": (
            [
                1,
                3,
                5,
                7,
                9,
                11,
                13,
                15,
                17,
                19,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
            10,
            [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
            10,
        ),
        "expected": [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
        ],
        "comparator": merge_comparator,
    },
    {
        "name": "Edge case: m=0, n=1, nums1 is [0], nums2 is [1]",
        "args": ([0], 0, [1], 1),
        "expected": [1],
        "comparator": merge_comparator,
    },
    {
        "name": "Edge case: m=1, n=0, nums1 is [1], nums2 is []",
        "args": ([1], 1, [], 0),
        "expected": [1],
        "comparator": merge_comparator,
    },
    {
        "name": "Negative numbers",
        "args": ([-5, -3, -1, 0, 0, 0], 3, [-4, -2, 0], 3),
        "expected": [-5, -4, -3, -2, -1, 0],
        "comparator": merge_comparator,
    },
]

# DEFAULT_TIMEOUT is optional
# DEFAULT_TIMEOUT = 1.0 # Set a 1-second default timeout for all tests in this file
