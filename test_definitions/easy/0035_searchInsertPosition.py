from typing import List, Dict, Any, Tuple

# METHOD_NAME is required
METHOD_NAME = "searchInsert"

# TEST_CASES is required
TEST_CASES: List[Dict[str, Any]] = [
    {
        "name": "Example 1: Target found in middle",
        "args": ([1, 3, 5, 6], 5),
        "expected": 2,
    },
    {
        "name": "Example 2: Target not found, insert in middle",
        "args": ([1, 3, 5, 6], 2),
        "expected": 1,
    },
    {
        "name": "Example 3: Target not found, insert at end",
        "args": ([1, 3, 5, 6], 7),
        "expected": 4,
    },
    {
        "name": "Target at beginning, found",
        "args": ([1, 3, 5, 6], 1),
        "expected": 0,
    },
    {
        "name": "Target at beginning, not found (insert 0)",
        "args": ([1, 3, 5, 6], 0),
        "expected": 0,
    },
    {
        "name": "Target at end, found",
        "args": ([1, 3, 5, 6], 6),
        "expected": 3,
    },
    {
        "name": "Empty array, insert at 0",
        "args": ([], 5),
        "expected": 0,
    },
    {
        "name": "Single element array, target found",
        "args": ([5], 5),
        "expected": 0,
    },
    {
        "name": "Single element array, target smaller (insert 0)",
        "args": ([5], 2),
        "expected": 0,
    },
    {
        "name": "Single element array, target larger (insert 1)",
        "args": ([5], 7),
        "expected": 1,
    },
    {
        "name": "Array with two elements, target found at 0",
        "args": ([2, 4], 2),
        "expected": 0,
    },
    {
        "name": "Array with two elements, target found at 1",
        "args": ([2, 4], 4),
        "expected": 1,
    },
    {
        "name": "Array with two elements, insert between",
        "args": ([2, 4], 3),
        "expected": 1,
    },
    {
        "name": "Array with two elements, insert before",
        "args": ([2, 4], 1),
        "expected": 0,
    },
    {
        "name": "Array with two elements, insert after",
        "args": ([2, 4], 5),
        "expected": 2,
    },
    {
        "name": "Long array, target found in middle",
        "args": ([i for i in range(1, 100, 2)], 51),  # [1,3,5,...,99]
        "expected": 25,  # 51 is the 26th element, 0-indexed is 25
    },
    {
        "name": "Long array, target not found, insert in middle",
        "args": ([i for i in range(1, 100, 2)], 50),
        "expected": 25,  # Would insert before 51 (index 25)
    },
    {
        "name": "Long array, target not found, insert at beginning",
        "args": ([i for i in range(10, 20)], 5),
        "expected": 0,
    },
    {
        "name": "Long array, target not found, insert at end",
        "args": ([i for i in range(10, 20)], 25),
        "expected": 10,
    },
    {
        "name": "Array with negative numbers, target found",
        "args": ([-5, -2, 0, 3, 7], -2),
        "expected": 1,
    },
    {
        "name": "Array with negative numbers, target not found, insert positive",
        "args": ([-5, -2, 0, 3, 7], 1),
        "expected": 3,
    },
    {
        "name": "Array with negative numbers, target not found, insert negative",
        "args": ([-5, -2, 0, 3, 7], -3),
        "expected": 1,
    },
    {
        "name": "Target is largest possible value",
        "args": ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10),
        "expected": 9,
    },
    {
        "name": "Target is smallest possible value",
        "args": ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1),
        "expected": 0,
    },
    {
        "name": "All elements large, target found",
        "args": ([100, 200, 300, 400], 300),
        "expected": 2,
    },
    {
        "name": "All elements large, target to insert",
        "args": ([100, 200, 300, 400], 250),
        "expected": 2,
    },
]
