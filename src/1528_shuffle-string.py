class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [''] * len(s)

        for idx, char in enumerate(s):
            result[indices[idx]] = char

        return ''.join(result)
