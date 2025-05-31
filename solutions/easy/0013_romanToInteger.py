class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        checkNext = ["I", "X", "C"]
        result = 0
        i = 0
        while i < len(s):
            letter = s[i]
            if letter in checkNext and i < len(s) - 1 and s[i : i + 2] in nums:
                result += nums[s[i : i + 2]]
                i += 2
                continue
            result += nums[letter]
            i += 1
        return result
