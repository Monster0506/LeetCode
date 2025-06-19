from typing import List, Dict, Any, Tuple, Optional, Callable
from framework import TreeNode  # Assuming TreeNode is available from framework

# METHOD_NAME is required
METHOD_NAME = "sortedArrayToBST"


# Helper functions for the custom comparator
def get_height(node: Optional[TreeNode]) -> int:
    """Calculates the height of a binary tree."""
    if not node:
        return 0
    return 1 + max(get_height(node.left), get_height(node.right))


def is_balanced(node: Optional[TreeNode]) -> bool:
    """Checks if a binary tree is height-balanced."""
    if not node:
        return True

    left_height = get_height(node.left)
    right_height = get_height(node.right)

    # Check the balance condition for the current node
    if abs(left_height - right_height) > 1:
        return False

    # Recursively check left and right subtrees
    return is_balanced(node.left) and is_balanced(node.right)


def inorder_traversal_list(node: Optional[TreeNode]) -> List[int]:
    """Performs an in-order traversal and returns a list of node values."""
    result = []
    if node:
        result.extend(inorder_traversal_list(node.left))
        result.append(node.val)
        result.extend(inorder_traversal_list(node.right))
    return result


# Custom comparator function for this problem
def custom_bst_comparator(
    actual_root: Optional[TreeNode],
    expected_placeholder: Any,
    all_args_after_call: Tuple,
) -> bool:
    """
    Compares the generated BST for correctness:
    1. It must be height-balanced.
    2. Its in-order traversal must match the original sorted input array
       (which implicitly checks the BST property and element correctness).
    """
    # The original input array is the first argument passed to the solution method
    input_nums = all_args_after_call[0]

    # Constraint: 1 <= nums.length <= 104, so input_nums will never be empty.
    # Therefore, actual_root should never be None.
    if not actual_root:
        print(f"  Comparator: Expected a TreeNode object, but received None.")
        return False

    # 1. Check if the generated tree is height-balanced
    if not is_balanced(actual_root):
        print(f"  Comparator: Generated tree is not height-balanced.")
        # Optionally, print details about height mismatch
        # print(f"    Root: {actual_root.val}, Left Height: {get_height(actual_root.left)}, Right Height: {get_height(actual_root.right)}")
        return False

    # 2. Perform in-order traversal to check BST property and content
    # For a valid BST, an in-order traversal should yield elements in sorted order.
    # This sorted order must exactly match the original input_nums.
    traversed_elements = inorder_traversal_list(actual_root)
    if traversed_elements != input_nums:
        print(
            f"  Comparator: In-order traversal of the generated tree "
            f"does not match the original sorted array (BST property or content mismatch)."
            f"\n    Original Input (Expected In-order): {input_nums}"
            f"\n    Actual In-order Traversal:          {traversed_elements}"
        )
        return False

    # If both checks pass, the generated tree is a valid solution
    return True


# TEST_CASES is required
TEST_CASES: List[Dict[str, Any]] = [
    {
        "name": "Example 1: Odd length array, 5 elements",
        "args": ([-10, -3, 0, 5, 9],),
        "expected": True,  # Placeholder, custom comparator does the check
        "comparator": custom_bst_comparator,
    },
    {
        "name": "Example 2: Even length array, 2 elements",
        "args": ([1, 3],),
        "expected": True,
        "comparator": custom_bst_comparator,
    },
    {
        "name": "Single element array",
        "args": ([0],),
        "expected": True,
        "comparator": custom_bst_comparator,
    },
    {
        "name": "Array with 4 elements (even length)",
        "args": ([1, 2, 3, 4],),
        "expected": True,
        "comparator": custom_bst_comparator,
    },
    {
        "name": "Array with 7 elements (odd length), complete tree",
        "args": ([1, 2, 3, 4, 5, 6, 7],),
        "expected": True,
        "comparator": custom_bst_comparator,
    },
    {
        "name": "Only negative numbers",
        "args": ([-5, -4, -3, -2, -1],),
        "expected": True,
        "comparator": custom_bst_comparator,
    },
    {
        "name": "Only positive numbers",
        "args": ([10, 20, 30, 40, 50],),
        "expected": True,
        "comparator": custom_bst_comparator,
    },
    {
        "name": "Mixed negative, zero, positive",
        "args": ([-2, -1, 0, 1, 2],),
        "expected": True,
        "comparator": custom_bst_comparator,
    },
    {
        "name": "Values at constraint boundaries",
        "args": ([-100, -50, 0, 50, 100],),
        "expected": True,
        "comparator": custom_bst_comparator,
    },
    {
        "name": "Longer array, 11 elements (odd length)",
        "args": ([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5],),
        "expected": True,
        "comparator": custom_bst_comparator,
    },
    {
        "name": "Longer array, 10 elements (even length)",
        "args": ([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4],),
        "expected": True,
        "comparator": custom_bst_comparator,
    },
    {
        "name": "Array with 6 elements",
        "args": ([1, 2, 3, 4, 5, 6],),
        "expected": True,
        "comparator": custom_bst_comparator,
    },
    {
        "name": "Array with values increasing rapidly",
        "args": ([1, 10, 100, 1000, 10000],),
        "expected": True,
        "comparator": custom_bst_comparator,
    },
    {
        "name": "Array with values decreasing rapidly (still sorted ascending)",
        "args": ([-10000, -1000, -100, -10, -1],),
        "expected": True,
        "comparator": custom_bst_comparator,
    },
    {
        "name": "Large array (50 elements) with distinct values",
        "args": ([i for i in range(50)],),
        "expected": True,
        "comparator": custom_bst_comparator,
    },
    {
        "name": "Large array (51 elements) with distinct values",
        "args": ([i for i in range(51)],),
        "expected": True,
        "comparator": custom_bst_comparator,
    },
    {
        "name": "Array with two elements - option 1 ([1,3] -> [3,1])",
        "args": ([1, 3],),
        "expected": True,
        "comparator": custom_bst_comparator,
    },
    {
        "name": "Array with two elements - option 2 ([1,3] -> [1,null,3])",
        "args": ([1, 3],),
        "expected": True,  # This case would still pass if [3,1] is built
        "comparator": custom_bst_comparator,
    },
]

# DEFAULT_TIMEOUT is optional. Constraints are relatively small, 10^4 nodes.
# DEFAULT_TIMEOUT = 1.0
