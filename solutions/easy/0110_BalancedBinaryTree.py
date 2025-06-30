from framework import TreeNode
from typing import Optional


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def getHeightAndBalance(node: Optional[TreeNode]) -> tuple[int, bool]:
            if node is None:
                return 0, True
            left_height, left_balanced = getHeightAndBalance(node.left)
            right_height, right_balanced = getHeightAndBalance(node.right)
            current_is_balanced = (
                abs(left_height - right_height) <= 1
                and left_balanced
                and right_balanced
            )
            return 1 + max(left_height, right_height), current_is_balanced

        return getHeightAndBalance(root)[1]
