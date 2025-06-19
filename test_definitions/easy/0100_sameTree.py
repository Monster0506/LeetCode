from typing import List, Dict, Any, Tuple, Optional
from framework import list_to_treenode

# METHOD_NAME is required
METHOD_NAME = "isSameTree"

# TEST_CASES is required
TEST_CASES: List[Dict[str, Any]] = [
    {
        "name": "Example 1: Identical trees",
        "args": (list_to_treenode([1, 2, 3]), list_to_treenode([1, 2, 3])),
        "expected": True,
    },
    {
        "name": "Example 2: Different structure (left child vs right child)",
        "args": (list_to_treenode([1, 2]), list_to_treenode([1, None, 2])),
        "expected": False,
    },
    {
        "name": "Example 3: Same structure, different values",
        "args": (list_to_treenode([1, 2, 1]), list_to_treenode([1, 1, 2])),
        "expected": False,
    },
    {
        "name": "Both empty trees",
        "args": (list_to_treenode([]), list_to_treenode([])),
        "expected": True,
    },
    {
        "name": "One empty tree, one non-empty",
        "args": (list_to_treenode([1]), list_to_treenode([])),
        "expected": False,
    },
    {
        "name": "Non-empty, one empty tree",
        "args": (list_to_treenode([]), list_to_treenode([1])),
        "expected": False,
    },
    {
        "name": "Single identical nodes",
        "args": (list_to_treenode([5]), list_to_treenode([5])),
        "expected": True,
    },
    {
        "name": "Single different nodes",
        "args": (list_to_treenode([5]), list_to_treenode([6])),
        "expected": False,
    },
    {
        "name": "Identical complete trees",
        "args": (
            list_to_treenode([1, 2, 3, 4, 5, 6, 7]),
            list_to_treenode([1, 2, 3, 4, 5, 6, 7]),
        ),
        "expected": True,
    },
    {
        "name": "Identical left-skewed trees",
        "args": (
            list_to_treenode([1, 2, None, 3, None, 4]),
            list_to_treenode([1, 2, None, 3, None, 4]),
        ),
        "expected": True,
    },
    {
        "name": "Identical right-skewed trees",
        "args": (
            list_to_treenode([1, None, 2, None, 3, None, 4]),
            list_to_treenode([1, None, 2, None, 3, None, 4]),
        ),
        "expected": True,
    },
    {
        "name": "Different values in complex trees",
        "args": (
            list_to_treenode([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]),
            list_to_treenode([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 10]),
        ),  # 9 vs 10
        "expected": False,
    },
    {
        "name": "Different structures (left vs right child missing)",
        "args": (
            list_to_treenode([1, 2, 3]),
            list_to_treenode([1, 2, None, 3]),
        ),
        "expected": False,
    },
    {
        "name": "Trees with negative values, identical",
        "args": (
            list_to_treenode([-1, -2, -3, -4, -5]),
            list_to_treenode([-1, -2, -3, -4, -5]),
        ),
        "expected": True,
    },
    {
        "name": "Trees with negative values, different values",
        "args": (
            list_to_treenode([-1, -2, -3]),
            list_to_treenode([-1, -2, -4]),
        ),
        "expected": False,
    },
    {
        "name": "Trees with 0 values, identical",
        "args": (
            list_to_treenode([0, 0, None, 0, 0]),
            list_to_treenode([0, 0, None, 0, 0]),
        ),
        "expected": True,
    },
    {
        "name": "Trees with 0 values, different structure",
        "args": (
            list_to_treenode([0, 0, 0]),
            list_to_treenode([0, 0, None, 0]),
        ),
        "expected": False,
    },
    # --- Additional Test Cases ---
    {
        "name": "Two symmetric but non-identical trees",
        "args": (
            list_to_treenode([1, 2, 2, 3, 4, 4, 3]),
            list_to_treenode([1, 2, 2, 3, 4, 3, 4]),
        ),
        "expected": False,
    },
    {
        "name": "Root values differ, rest is identical structure",
        "args": (
            list_to_treenode([1, 2, 3]),
            list_to_treenode([10, 2, 3]),
        ),
        "expected": False,
    },
    {
        "name": "One tree missing a leaf node",
        "args": (
            list_to_treenode([1, 2, 3, 4]),
            list_to_treenode([1, 2, 3]),
        ),
        "expected": False,
    },
    {
        "name": "One tree has an extra leaf node",
        "args": (
            list_to_treenode([1, 2, 3]),
            list_to_treenode([1, 2, 3, 4]),
        ),
        "expected": False,
    },
    {
        "name": "Trees with max/min constraint values, identical",
        "args": (
            list_to_treenode([-100, 0, 100]),
            list_to_treenode([-100, 0, 100]),
        ),
        "expected": True,
    },
    {
        "name": "Trees with max/min constraint values, different",
        "args": (
            list_to_treenode([-100, 0, 100]),
            list_to_treenode([-100, 0, 99]),
        ),
        "expected": False,
    },
    {
        "name": "Longer identical trees with mixed nulls",
        "args": (
            list_to_treenode([5, 4, 7, 3, None, 6, 8, None, 2]),
            list_to_treenode([5, 4, 7, 3, None, 6, 8, None, 2]),
        ),
        "expected": True,
    },
    {
        "name": "Longer different trees with mixed nulls (value mismatch)",
        "args": (
            list_to_treenode([5, 4, 7, 3, None, 6, 8, None, 2]),
            list_to_treenode([5, 4, 7, 3, None, 6, 8, None, 99]),
        ),
        "expected": False,
    },
    {
        "name": "Longer different trees with mixed nulls (structure mismatch)",
        "args": (
            list_to_treenode([5, 4, 7, 3, None, 6, 8, None, 2]),
            list_to_treenode(
                [5, 4, 7, 3, None, 6, 8, 2]
            ),  # Missing one 'None' for structure
        ),
        "expected": False,
    },
    {
        "name": "Only left child, same",
        "args": (list_to_treenode([1, 2]), list_to_treenode([1, 2])),
        "expected": True,
    },
    {
        "name": "Only right child, same",
        "args": (list_to_treenode([1, None, 2]), list_to_treenode([1, None, 2])),
        "expected": True,
    },
    {
        "name": "Only left child vs only right child, different",
        "args": (list_to_treenode([1, 2]), list_to_treenode([1, None, 2])),
        "expected": False,
    },
]

# DEFAULT_TIMEOUT is optional. Constraints are small, so not strictly necessary.
# DEFAULT_TIMEOUT = 1.0
