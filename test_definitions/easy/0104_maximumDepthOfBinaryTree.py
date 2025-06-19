from typing import List, Dict, Any
from framework import list_to_treenode

# METHOD_NAME is required
METHOD_NAME = "maxDepth"

# TEST_CASES is required
TEST_CASES: List[Dict[str, Any]] = [
    {
        "name": "Example 1: Standard tree",
        "args": (list_to_treenode([3, 9, 20, None, None, 15, 7]),),
        "expected": 3,
    },
    {
        "name": "Example 2: Right-skewed tree (partial)",
        "args": (list_to_treenode([1, None, 2]),),
        "expected": 2,
    },
    {
        "name": "Empty tree",
        "args": (list_to_treenode([]),),
        "expected": 0,
    },
    {
        "name": "Single node tree",
        "args": (list_to_treenode([0]),),
        "expected": 1,
    },
    {
        "name": "Left-skewed tree",
        "args": (list_to_treenode([1, 2, None, 3, None, 4]),),
        "expected": 4,
    },
    {
        "name": "Right-skewed tree (full)",
        "args": (list_to_treenode([1, None, 2, None, 3, None, 4]),),
        "expected": 4,
    },
    {
        "name": "Complete binary tree of depth 3",
        "args": (list_to_treenode([1, 2, 3, 4, 5, 6, 7]),),
        "expected": 3,
    },
    {
        "name": "Tree with left subtree deeper",
        "args": (list_to_treenode([1, 2, 3, 4, None, None, None, 5]),),
        "expected": 4,
    },
    {
        "name": "Tree with mixed negative/positive values",
        "args": (list_to_treenode([-1, -2, 0, 1, 2, 3, 4, -5, 6, -7]),),
        "expected": 4,
    },
    {
        "name": "Max constraint depth (104 nodes, nearly linear)",
        # Represents a linear chain of 100 nodes for max depth
        "args": (
            list_to_treenode(
                [i for i in range(1, 101)]
                + [None] * (100 * 2 - len(list(range(1, 101))))
            ),
        ),
        "expected": 7,
    },
    # --- Additional Test Cases ---
    {
        "name": "Two nodes, linear left branch",
        "args": (list_to_treenode([1, 2]),),
        "expected": 2,
    },
    {
        "name": "Depth 3, only left branch",
        "args": (list_to_treenode([1, 2, None, 3]),),
        "expected": 3,
    },
    {
        "name": "Depth 3, only right branch",
        "args": (list_to_treenode([1, None, 2, None, 3]),),
        "expected": 3,
    },
    {
        "name": "Depth 4, left subtree deeper (non-sequential values)",
        "args": (list_to_treenode([10, 20, 30, 40, None, None, None, 50]),),
        "expected": 4,  # Path: 10 -> 20 -> 40 -> 50
    },
    {
        "name": "Moderately complex tree, depth 4",
        "args": (list_to_treenode([1, 2, 3, 4, 5, None, 6, 7, 8]),),
        "expected": 4,  # Paths: 1-2-4-7, 1-2-4-8, 1-2-5, 1-3-6
    },
    {
        "name": "Tree with intermediate nulls but deep branches",
        "args": (list_to_treenode([1, 2, None, None, 3, 4, None, None, 5]),),
        "expected": 5,
    },
]

# DEFAULT_TIMEOUT is optional; problem constraints allow for quick execution.
# DEFAULT_TIMEOUT = 1.0
