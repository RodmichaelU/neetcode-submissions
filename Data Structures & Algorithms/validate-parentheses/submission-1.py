class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracket = {
            "}": "{",
            "]":"[",
            ")":"("
        }

        for i in s:
            if i in bracket:
                if not stack or stack[-1] != bracket[i]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)

        if not stack:
            return True
        else:
            return False