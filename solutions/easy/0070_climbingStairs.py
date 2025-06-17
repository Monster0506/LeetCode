from typing import Dict


class Solution:
    def climbStairs(self, n: int) -> int:

        def climbStairsHelper(n: int, seen: Dict[int, int]):
            if n <= 1:
                return 1
            if n in seen:
                return seen[n]
            seen[n] = climbStairsHelper(n - 1, seen) + climbStairsHelper(n - 2, seen)
            return seen[n]

        seen = {}
        return climbStairsHelper(n, seen)
