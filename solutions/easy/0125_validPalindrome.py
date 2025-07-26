class Solution:
    def isPalindrome(self, s: str) -> bool:
        charMap = [c.lower() for c in s if c.isalnum()]
        return charMap[::-1] == charMap
