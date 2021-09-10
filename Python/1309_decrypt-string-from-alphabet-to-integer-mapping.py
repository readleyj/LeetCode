class Solution:
    def freqAlphabets(self, s: str) -> str:
        mapping, idx = '', 0

        while idx < len(s):
            if idx + 2 < len(s) and s[idx + 2] == '#':
                int_code = int(s[idx] + s[idx + 1])
                idx += 2
            else:
                int_code = int(s[idx])

            idx += 1
            mapping += ascii_lowercase[int_code - 1]

        return mapping
