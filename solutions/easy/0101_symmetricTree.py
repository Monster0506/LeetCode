from framework import TreeNode, pretty_print_tree
from typing import Optional


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        pretty_print_tree(root)

        def helper(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False
            return (
                node1.val == node2.val
                and helper(node1.left, node2.right)
                and helper(node2.left, node1.right)
            )

        if root is None:
            return True
        return helper(root.left, root.right)
