class Solution:
    def balancedStringSplit(self, s: str) -> int:
        running_count, result = 0, 0

        for char in s:
            running_count += 1 if char == 'R' else -1

            if running_count == 0:
                result += 1

        return result
