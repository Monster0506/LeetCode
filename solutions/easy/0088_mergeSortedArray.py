from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i, j = m - 1, n - 1
        pMerged = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[pMerged] = nums1[i]
                i -= 1
                pMerged -= 1
            else:
                nums1[pMerged] = nums2[j]
                j -= 1
                pMerged -= 1
        if j >= 0:
            nums1[: j + 1] = nums2[: j + 1]
