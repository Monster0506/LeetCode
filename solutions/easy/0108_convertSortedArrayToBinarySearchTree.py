from typing import List, Optional
from framework import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        length = len(nums)
        if length == 1:
            return TreeNode(nums[0])
        if length == 0:
            return None

        mid = length // 2
        item = TreeNode(nums[mid])
        item.left = self.sortedArrayToBST(nums[:mid])
        item.right = self.sortedArrayToBST(nums[mid + 1 :])
        return item
