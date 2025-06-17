from typing import Tuple


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a.rjust(max(len(a), len(b)), "0")
        b = b.rjust(max(len(a), len(b)), "0")
        solution = []
        carry = "0"
        for i in range(len(a) - 1, -1, -1):
            ans, carry = self.helper(a[i], b[i], carry)
            solution.insert(0, ans)

        if carry == "1":
            solution.insert(0, carry)
        return "".join(solution)

    def helper(self, a: str, b: str, carry: str) -> Tuple[str, str]:
        data = {
            "000": ("0", "0"),
            "001": ("1", "0"),
            "010": ("1", "0"),
            "011": ("0", "1"),
            "100": ("1", "0"),
            "101": ("0", "1"),
            "110": ("0", "1"),
            "111": ("1", "1"),
        }
        return data[a + b + carry]
