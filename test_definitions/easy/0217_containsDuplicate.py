from typing import Any, Dict, List, Tuple


# METHOD_NAME is required
METHOD_NAME = "containsDuplicate"

# TEST_CASES is required
TEST_CASES: List[Dict[str, Any]] = [
    {
        "name": "Example 1: Basic duplicate",
        "args": ([1, 2, 3, 1],),
        "expected": True,
    },
    {
        "name": "Example 2: All distinct",
        "args": ([1, 2, 3, 4],),
        "expected": False,
    },
    {
        "name": "Example 3: Multiple duplicates",
        "args": ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2],),
        "expected": True,
    },
    {
        "name": "Single element array (no duplicate possible)",
        "args": ([5],),
        "expected": False,
    },
    {
        "name": "Two elements, duplicate",
        "args": ([7, 7],),
        "expected": True,
    },
    {
        "name": "Two elements, distinct",
        "args": ([7, 8],),
        "expected": False,
    },
    {
        "name": "All elements are duplicates of one value",
        "args": ([10, 10, 10, 10, 10],),
        "expected": True,
    },
    {
        "name": "Array with zero and negative numbers, distinct",
        "args": ([-5, 0, 1, 100],),
        "expected": False,
    },
    {
        "name": "Array with zero and negative numbers, duplicate",
        "args": ([-5, 0, 1, -5, 100],),
        "expected": True,
    },
    {
        "name": "Duplicate at the start",
        "args": ([2, 2, 3, 4, 5],),
        "expected": True,
    },
    {
        "name": "Duplicate at the end",
        "args": ([1, 2, 3, 4, 4],),
        "expected": True,
    },
    {
        "name": "Duplicate in the middle",
        "args": ([1, 2, 4, 4, 5],),
        "expected": True,
    },
    {
        "name": "Large numbers, distinct",
        "args": ([-1000000000, 0, 1000000000],),
        "expected": False,
    },
    {
        "name": "Large numbers, duplicate",
        "args": ([-1000000000, 0, 1000000000, 0],),
        "expected": True,
    },
    {
        "name": "Long list, all unique",
        "args": (list(range(1000)),),  # 0 to 999
        "expected": False,
    },
    {
        "name": "Long list, with one duplicate at the end",
        "args": (list(range(1000)) + [999],),
        "expected": True,
    },
    {
        "name": "Long list, with one duplicate in the middle",
        "args": (list(range(500)) + [250] + list(range(500, 1000)),),
        "expected": True,
    },
    {
        "name": "List with multiple distinct duplicates",
        "args": ([1, 2, 1, 3, 4, 2, 5, 3],),
        "expected": True,
    },
]

# DEFAULT_TIMEOUT is optional. Constraints allow for quick execution.
# DEFAULT_TIMEOUT = 1.0
