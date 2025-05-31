class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        st = str(x)
        if len(st) == 1:
            return True
        return st == st[::-1]
