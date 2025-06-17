from typing import List, Dict, Any, Tuple, Optional
from framework import list_to_treenode

# METHOD_NAME is required
METHOD_NAME = "inorderTraversal"

# TEST_CASES is required
TEST_CASES: List[Dict[str, Any]] = [
    {
        "name": "Example 1: Basic tree",
        "args": (list_to_treenode([1, None, 2, 3]),),
        "expected": [1, 3, 2],
    },
    {
        "name": "Example 2: Complex tree",
        "args": (list_to_treenode([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]),),
        "expected": [4, 2, 6, 5, 7, 1, 3, 9, 8],
    },
    {
        "name": "Example 3: Empty tree",
        "args": (list_to_treenode([]),),
        "expected": [],
    },
    {
        "name": "Example 4: Single node tree",
        "args": (list_to_treenode([1]),),
        "expected": [1],
    },
    {
        "name": "Left-skewed tree",
        "args": (list_to_treenode([1, 2, None, 3, None, 4]),),
        "expected": [4, 3, 2, 1],
    },
    {
        "name": "Right-skewed tree",
        "args": (list_to_treenode([1, None, 2, None, 3, None, 4]),),
        "expected": [1, 2, 3, 4],
    },
    {
        "name": "Complete binary tree",
        "args": (list_to_treenode([1, 2, 3, 4, 5, 6, 7]),),
        "expected": [4, 2, 5, 1, 6, 3, 7],
    },
    {
        "name": "Tree with negative values",
        "args": (list_to_treenode([-1, -2, -3, -4, -5]),),
        "expected": [-4, -2, -5, -1, -3],
    },
    {
        "name": "Tree with zero values",
        "args": (list_to_treenode([0, 0, 0, None, None, 0, 0]),),
        "expected": [0, 0, 0, 0, 0],
    },
    {
        "name": "Tree with only left children (zigzag nulls)",
        "args": (list_to_treenode([10, 5, None, 2, None, 1]),),
        "expected": [1, 2, 5, 10],
    },
    {
        "name": "Tree with only right children (zigzag nulls)",
        "args": (list_to_treenode([10, None, 15, None, 20, None, 25]),),
        "expected": [10, 15, 20, 25],
    },
]

# DEFAULT_TIMEOUT is optional; problem constraints are small.
# DEFAULT_TIMEOUT = 1.0
