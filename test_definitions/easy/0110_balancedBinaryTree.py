from typing import List, Dict, Any, Tuple, Optional
from framework import list_to_treenode

# METHOD_NAME is required
METHOD_NAME = "isBalanced"

# TEST_CASES is required
TEST_CASES: List[Dict[str, Any]] = [
    {
        "name": "Example 1: Balanced tree",
        "args": (list_to_treenode([3, 9, 20, None, None, 15, 7]),),
        "expected": True,
    },
    {
        "name": "Example 2: Unbalanced tree (left subtree too deep)",
        "args": (list_to_treenode([1, 2, 2, 3, 3, None, None, 4, 4]),),
        "expected": False,
    },
    {
        "name": "Example 3: Empty tree",
        "args": (list_to_treenode([]),),
        "expected": True,
    },
    {
        "name": "Single node tree",
        "args": (list_to_treenode([1]),),
        "expected": True,
    },
    {
        "name": "Two nodes: balanced (linear)",
        "args": (list_to_treenode([1, 2]),),
        "expected": True,
    },
    {
        "name": "Two levels: perfectly balanced",
        "args": (list_to_treenode([1, 2, 3]),),
        "expected": True,
    },
    {
        "name": "Unbalanced: Left-skewed (diff 2)",
        "args": (list_to_treenode([1, 2, None, 3]),),
        "expected": False,
    },
    {
        "name": "Unbalanced: Left-skewed (diff 2)",
        "args": (list_to_treenode([1, None, 2, None, 3]),),
        "expected": False,
    },
    {
        "name": "Unbalanced: Left-skewed (diff 2)",
        "args": (list_to_treenode([1, 2, None, 3, None, 4]),),
        "expected": False,
    },
    {
        "name": "Unbalanced: Right-skewed (diff 2)",
        "args": (list_to_treenode([1, None, 2, None, 3, None, 4]),),
        "expected": False,
    },
    {
        "name": "Balanced: Complete tree, depth 3",
        "args": (list_to_treenode([1, 2, 3, 4, 5, 6, 7]),),
        "expected": True,
    },
    {
        "name": "Unbalanced: Left side much deeper",
        "args": (
            list_to_treenode([1, 2, 3, 4, None, None, None, 5, 6, None, None, 7]),
        ),
        "expected": False,  # Depth of left subtree (5) vs right (1) for root 1
    },
    {
        "name": "Unbalanced: Right side much deeper",
        "args": (
            list_to_treenode([1, 2, 3, None, None, 4, 5, None, None, 6, None, None, 7]),
        ),
        "expected": False,  # Depth of right subtree (5) vs left (1) for root 1
    },
    {
        "name": "Balanced: Mixed values, simple",
        "args": (list_to_treenode([-100, 0, 100]),),
        "expected": True,
    },
    {
        "name": "Balanced: All same value nodes",
        "args": (list_to_treenode([7, 7, 7, 7, 7, 7, 7]),),
        "expected": True,
    },
    {
        "name": "Unbalanced: Subtree imbalance (left child of root)",
        "args": (
            list_to_treenode(
                [1, 2, 3, 4, None, None, None, 5, 6]
            ),  # Left child 2 has a subtree of depth 3, but right child is None
        ),
        "expected": False,
    },
    {
        "name": "Unbalanced: Subtree imbalance (right child of root)",
        "args": (
            list_to_treenode(
                [1, 2, 3, None, 4, None, None, None, 5]
            ),  # Right child 3 has a subtree of depth 3, but left child is None
        ),
        "expected": False,
    },
    {
        "name": "Balanced: Moderately complex, depth 4",
        "args": (
            list_to_treenode([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),
        ),
        "expected": True,
    },
    {
        "name": "Unbalanced: Large tree, small difference propagates to root",
        "args": (
            list_to_treenode(
                [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    None,
                    7,
                    8,
                    9,
                    10,
                    11,
                    12,
                    None,
                    None,
                    None,
                    None,
                    13,
                    14,
                ]
            ),
        ),
        "expected": False,  # Root 1: left (depth 5 via 2-4-7-13) vs right (depth 3 via 3-6)
    },
    {
        "name": "Balanced: Max nodes, perfectly balanced (approx)",
        # For a truly balanced tree of ~5000 nodes, it would be a complete binary tree.
        # This simulates a deep, but generally balanced structure.
        # This specific list is for a complete binary tree of depth ~12 (2^12 - 1 nodes)
        # Using a slice to fit the 5000 constraint if it's too large.
        "args": (list_to_treenode([i for i in range(1, 5001)]),),
        "expected": True,
    },
    {
        "name": "Balanced: Max nodes",
        "args": (
            list_to_treenode(
                [i for i in range(1, 5001)]
                + [None] * (5000 * 2 - len(list(range(1, 5001))))
            ),
        ),  # Represents a linear tree of 5000 nodes, depth 5000
        "expected": True,
    },
]

# DEFAULT_TIMEOUT is optional. Constraints are relatively generous for a tree traversal.
# DEFAULT_TIMEOUT = 1.0
