from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for char in s:
            if char in ["(", "[", "{"]:
                stack.append(char)
            else:
                if len(stack) < 1:
                    return False
                match char:
                    case ")":
                        if stack.pop() != "(":
                            return False

                    case "]":
                        if stack.pop() != "[":
                            return False
                    case "}":
                        if stack.pop() != "{":
                            return False
                    case _:
                        pass

        return len(stack) == 0
