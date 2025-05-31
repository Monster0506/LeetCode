from typing import List, Dict, Any, Optional

from framework import ListNode, list_to_linkedlist

# The exact name of the method to test in the Solution class
METHOD_NAME = "mergeTwoLists"

# The list of test cases for this problem
TEST_CASES: List[Dict[str, Any]] = [
    {
        "name": "LeetCode Example 1",
        "args": (
            list_to_linkedlist([1, 2, 4]),
            list_to_linkedlist([1, 3, 4]),
        ),
        "expected": list_to_linkedlist([1, 1, 2, 3, 4, 4]),
    },
    {
        "name": "LeetCode Example 2: Both lists empty",
        "args": (list_to_linkedlist([]), list_to_linkedlist([])),
        "expected": list_to_linkedlist([]),
    },
    {
        "name": "LeetCode Example 3: list1 empty, list2 has one node",
        "args": (list_to_linkedlist([]), list_to_linkedlist([0])),
        "expected": list_to_linkedlist([0]),
    },
    {
        "name": "list2 empty, list1 has one node",
        "args": (list_to_linkedlist([0]), list_to_linkedlist([])),
        "expected": list_to_linkedlist([0]),
    },
    {
        "name": "Both lists have one node, list1 smaller",
        "args": (list_to_linkedlist([1]), list_to_linkedlist([2])),
        "expected": list_to_linkedlist([1, 2]),
    },
    {
        "name": "Both lists have one node, list2 smaller",
        "args": (list_to_linkedlist([2]), list_to_linkedlist([1])),
        "expected": list_to_linkedlist([1, 2]),
    },
    {
        "name": "Both lists have one identical node",
        "args": (list_to_linkedlist([5]), list_to_linkedlist([5])),
        "expected": list_to_linkedlist([5, 5]),
    },
    {
        "name": "list1 shorter, all its elements smaller",
        "args": (
            list_to_linkedlist([1, 2]),
            list_to_linkedlist([3, 4, 5]),
        ),
        "expected": list_to_linkedlist([1, 2, 3, 4, 5]),
    },
    {
        "name": "list2 shorter, all its elements smaller",
        "args": (
            list_to_linkedlist([3, 4, 5]),
            list_to_linkedlist([1, 2]),
        ),
        "expected": list_to_linkedlist([1, 2, 3, 4, 5]),
    },
    {
        "name": "Interleaved values",
        "args": (
            list_to_linkedlist([1, 3, 5, 7]),
            list_to_linkedlist([2, 4, 6, 8]),
        ),
        "expected": list_to_linkedlist([1, 2, 3, 4, 5, 6, 7, 8]),
    },
    {
        "name": "Interleaved values, list2 starts smaller",
        "args": (
            list_to_linkedlist([2, 4, 6, 8]),
            list_to_linkedlist([1, 3, 5, 7]),
        ),
        "expected": list_to_linkedlist([1, 2, 3, 4, 5, 6, 7, 8]),
    },
    {
        "name": "Duplicates within and across lists",
        "args": (
            list_to_linkedlist([1, 1, 2, 5]),
            list_to_linkedlist([1, 3, 5, 5]),
        ),
        "expected": list_to_linkedlist([1, 1, 1, 2, 3, 5, 5, 5]),
    },
    {
        "name": "All elements in list1 are smaller than list2",
        "args": (
            list_to_linkedlist([10, 20, 30]),
            list_to_linkedlist([40, 50]),
        ),
        "expected": list_to_linkedlist([10, 20, 30, 40, 50]),
    },
    {
        "name": "All elements in list2 are smaller than list1",
        "args": (
            list_to_linkedlist([40, 50]),
            list_to_linkedlist([10, 20, 30]),
        ),
        "expected": list_to_linkedlist([10, 20, 30, 40, 50]),
    },
    {
        "name": "Negative numbers",
        "args": (
            list_to_linkedlist([-5, -2, -1]),
            list_to_linkedlist([-4, -3, 0]),
        ),
        "expected": list_to_linkedlist([-5, -4, -3, -2, -1, 0]),
    },
    {
        "name": "Mixed positive and negative numbers",
        "args": (
            list_to_linkedlist([-2, 0, 2]),
            list_to_linkedlist([-1, 1, 3]),
        ),
        "expected": list_to_linkedlist([-2, -1, 0, 1, 2, 3]),
    },
    {
        "name": "One list with zeros",
        "args": (
            list_to_linkedlist([0, 0, 0]),
            list_to_linkedlist([1, 2]),
        ),
        "expected": list_to_linkedlist([0, 0, 0, 1, 2]),
    },
    {
        "name": "Both lists with zeros",
        "args": (
            list_to_linkedlist([-1, 0, 0]),
            list_to_linkedlist([0, 0, 1]),
        ),
        "expected": list_to_linkedlist([-1, 0, 0, 0, 0, 1]),
    },
    {
        "name": "Longer list1, list2 empty",
        "args": (
            list_to_linkedlist([1, 2, 3, 4, 5]),
            list_to_linkedlist([]),
        ),
        "expected": list_to_linkedlist([1, 2, 3, 4, 5]),
    },
    {
        "name": "Longer list2, list1 empty",
        "args": (
            list_to_linkedlist([]),
            list_to_linkedlist([1, 2, 3, 4, 5]),
        ),
        "expected": list_to_linkedlist([1, 2, 3, 4, 5]),
    },
    {
        "name": "Identical lists",
        "args": (
            list_to_linkedlist([10, 20, 30]),
            list_to_linkedlist([10, 20, 30]),
        ),
        "expected": list_to_linkedlist([10, 10, 20, 20, 30, 30]),
    },
    {
        "name": "Max value constraint check (example values)",
        "args": (
            list_to_linkedlist([98, 99, 100]),
            list_to_linkedlist([99, 100]),
        ),
        "expected": list_to_linkedlist([98, 99, 99, 100, 100]),
    },
    {
        "name": "Min value constraint check (example values)",
        "args": (
            list_to_linkedlist([-100, -99]),
            list_to_linkedlist([-100, -98]),
        ),
        "expected": list_to_linkedlist([-100, -100, -99, -98]),
    },
]

# Optional: You can also define a default timeout for this specific problem's tests
# DEFAULT_TIMEOUT = 1.0  # seconds
