from framework import TreeNode
from typing import Optional


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        return (
            self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            if p and q and p.val == q.val
            else False
        )
