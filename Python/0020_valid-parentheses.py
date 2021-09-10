class Solution:
    MAPPING = {')': '(', ']': '[', '}': '{'}

    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in ')]}':
                if not stack:
                    return False

                if stack[-1] == self.MAPPING[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack
