from typing import List, Dict, Any
from framework import list_to_treenode

# METHOD_NAME is required
METHOD_NAME = "isSymmetric"

# TEST_CASES is required
TEST_CASES: List[Dict[str, Any]] = [
    {
        "name": "Example 1: Symmetric tree",
        "args": (list_to_treenode([1, 2, 2, 3, 4, 4, 3]),),
        "expected": True,
    },
    {
        "name": "Example 2: Non-symmetric tree (structure mismatch)",
        "args": (list_to_treenode([1, 2, 2, None, 3, None, 3]),),
        "expected": False,
    },
    {
        "name": "Single node tree",
        "args": (list_to_treenode([1]),),
        "expected": True,
    },
    {
        "name": "Two levels, perfectly symmetric",
        "args": (list_to_treenode([1, 2, 2]),),
        "expected": True,
    },
    {
        "name": "Two levels, non-symmetric (values)",
        "args": (list_to_treenode([1, 2, 3]),),
        "expected": False,
    },
    {
        "name": "Two levels, non-symmetric (structure - only left child)",
        "args": (list_to_treenode([1, 2]),),
        "expected": False,
    },
    {
        "name": "Two levels, non-symmetric (structure - only right child)",
        "args": (list_to_treenode([1, None, 2]),),
        "expected": False,
    },
    {
        "name": "Left-skewed tree (non-symmetric)",
        "args": (list_to_treenode([1, 2, None, 3, None, 4]),),
        "expected": False,
    },
    {
        "name": "Right-skewed tree (non-symmetric)",
        "args": (list_to_treenode([1, None, 2, None, 3, None, 4]),),
        "expected": False,
    },
    {
        "name": "Symmetric structure, but one value mismatch",
        "args": (list_to_treenode([1, 2, 2, 3, 4, 4, 5]),),  # 3 vs 5 mismatch
        "expected": False,
    },
    {
        "name": "Symmetric values, but structure mismatch (missing rightmost leaf)",
        "args": (
            list_to_treenode([1, 2, 2, 3, 4, 4]),
        ),  # Expected [1,2,2,3,4,4,3], here last 3 is missing
        "expected": False,
    },
    {
        "name": "Tree with negative values, symmetric",
        "args": (list_to_treenode([0, -1, -1, -2, -3, -3, -2]),),
        "expected": True,
    },
    {
        "name": "Tree with negative values, non-symmetric",
        "args": (list_to_treenode([0, -1, -1, -2, -3, -4, -2]),),
        "expected": False,
    },
    {
        "name": "Tree with zero values, symmetric",
        "args": (list_to_treenode([5, 0, 0, 0, None, None, 0]),),
        "expected": True,
    },
    {
        "name": "Tree with zero values, non-symmetric",
        "args": (
            list_to_treenode([5, 0, 0, 0, None, 0, 0]),
        ),  # right child of left 0 is 0, but right child of right 0 is None
        "expected": False,
    },
    {
        "name": "All same values, symmetric by definition",
        "args": (list_to_treenode([5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]),),
        "expected": True,
    },
    {
        "name": "Larger tree, perfectly symmetric",
        "args": (
            list_to_treenode(
                [10, 5, 5, 2, 3, 3, 2, 1, None, None, 4, 4, None, None, 1]
            ),
        ),
        "expected": True,
    },
    {
        "name": "Larger tree, subtly non-symmetric (deep value mismatch)",
        "args": (
            list_to_treenode(
                [10, 5, 5, 2, 3, 3, 2, 1, None, None, 4, 4, None, None, 99]
            ),  # Last 1 vs 99
        ),
        "expected": False,
    },
    {
        "name": "Larger tree, subtly non-symmetric (deep structure mismatch)",
        "args": (
            list_to_treenode(
                [10, 5, 5, 2, 3, 3, 2, 1, None, None, 4, 4, 1]
            ),  # right side's 2 has only a left child 1, but left side's 2 has left child 1 and right child None
        ),
        "expected": False,
    },
]

# DEFAULT_TIMEOUT is optional. Constraints are relatively small.
# DEFAULT_TIMEOUT = 1.0
