from framework import TreeNode
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return max(
                1 + depth(node.left),
                1 + depth(node.right),
            )

        return depth(root)
