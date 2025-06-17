from framework import TreeNode, pretty_print_tree

from typing import Optional, List


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        pretty_print_tree(root)
        result = []
        if not root:
            return []
        result.extend(self.inorderTraversal(root.left))

        result.append(root.val)

        result.extend(self.inorderTraversal(root.right))

        return result
