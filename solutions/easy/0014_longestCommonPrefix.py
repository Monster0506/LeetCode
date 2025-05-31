from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        minlen = min([len(s) for s in strs])
        currentLongest = ""
        potential_prefix = ""
        i = 0
        while i < minlen:
            potential_prefix = currentLongest + strs[0][i]
            for s in strs:
                if not s.startswith(potential_prefix):
                    return currentLongest
            currentLongest = potential_prefix
            i += 1

        return currentLongest
