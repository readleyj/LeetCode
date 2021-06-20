class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        result = list(s)
        left_idx, right_idx = 0, len(s) - 1

        while left_idx < right_idx:
            if not s[left_idx].isalpha():
                left_idx += 1
                continue

            if not s[right_idx].isalpha():
                right_idx += -1
                continue

            result[left_idx], result[right_idx] = s[right_idx], s[left_idx]
            left_idx, right_idx = left_idx + 1, right_idx - 1

        return ''.join(result)
