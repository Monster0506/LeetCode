from typing import List, Dict, Any, Tuple, Optional
from framework import list_to_linkedlist

# METHOD_NAME is required
METHOD_NAME = "deleteDuplicates"

# TEST_CASES is required
TEST_CASES: List[Dict[str, Any]] = [
    {
        "name": "Example 1: Basic duplicates",
        "args": (list_to_linkedlist([1, 1, 2]),),
        "expected": list_to_linkedlist([1, 2]),
    },
    {
        "name": "Example 2: Multiple duplicates",
        "args": (list_to_linkedlist([1, 1, 2, 3, 3]),),
        "expected": list_to_linkedlist([1, 2, 3]),
    },
    {
        "name": "No duplicates",
        "args": (list_to_linkedlist([1, 2, 3]),),
        "expected": list_to_linkedlist([1, 2, 3]),
    },
    {
        "name": "All duplicates",
        "args": (list_to_linkedlist([5, 5, 5, 5]),),
        "expected": list_to_linkedlist([5]),
    },
    {
        "name": "Single node list",
        "args": (list_to_linkedlist([0]),),
        "expected": list_to_linkedlist([0]),
    },
    {
        "name": "Empty list",
        "args": (list_to_linkedlist([]),),
        "expected": list_to_linkedlist([]),
    },
    {
        "name": "Two nodes, no duplicates",
        "args": (list_to_linkedlist([1, 2]),),
        "expected": list_to_linkedlist([1, 2]),
    },
    {
        "name": "Two nodes, duplicates",
        "args": (list_to_linkedlist([7, 7]),),
        "expected": list_to_linkedlist([7]),
    },
    {
        "name": "Longer list with various duplicates",
        "args": (list_to_linkedlist([-3, -3, 0, 0, 0, 1, 1, 1, 1, 2, 2, 5]),),
        "expected": list_to_linkedlist([-3, 0, 1, 2, 5]),
    },
    {
        "name": "List with negative values and duplicates",
        "args": (list_to_linkedlist([-5, -5, -4, -3, -3, -3, -1]),),
        "expected": list_to_linkedlist([-5, -4, -3, -1]),
    },
    # --- Additional Test Cases ---
    {
        "name": "Longer list, duplicates at start and end",
        "args": (list_to_linkedlist([1, 1, 1, 2, 3, 4, 4, 4]),),
        "expected": list_to_linkedlist([1, 2, 3, 4]),
    },
    {
        "name": "Consecutive duplicates throughout",
        "args": (list_to_linkedlist([1, 1, 2, 2, 3, 3, 4, 4]),),
        "expected": list_to_linkedlist([1, 2, 3, 4]),
    },
    {
        "name": "Values at boundaries of constraints",
        "args": (list_to_linkedlist([-100, -100, 0, 100, 100]),),
        "expected": list_to_linkedlist([-100, 0, 100]),
    },
    {
        "name": "Duplicates only at the head",
        "args": (list_to_linkedlist([1, 1, 1, 2, 3, 4]),),
        "expected": list_to_linkedlist([1, 2, 3, 4]),
    },
    {
        "name": "Duplicates only at the tail",
        "args": (list_to_linkedlist([1, 2, 3, 4, 4, 4]),),
        "expected": list_to_linkedlist([1, 2, 3, 4]),
    },
    {
        "name": "Mixed positive and negative, duplicates",
        "args": (list_to_linkedlist([-2, -2, -1, 0, 0, 1, 1, 2]),),
        "expected": list_to_linkedlist([-2, -1, 0, 1, 2]),
    },
    {
        "name": "Larger number of duplicate sequences",
        "args": (list_to_linkedlist([1, 1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5]),),
        "expected": list_to_linkedlist([1, 2, 3, 4, 5]),
    },
    {
        "name": "List with zero and duplicates",
        "args": (list_to_linkedlist([0, 0, 0, 1, 2]),),
        "expected": list_to_linkedlist([0, 1, 2]),
    },
]

# DEFAULT_TIMEOUT is optional; problem is small, so not strictly necessary.
# DEFAULT_TIMEOUT = 1.0
