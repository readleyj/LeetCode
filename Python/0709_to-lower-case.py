class Solution:
    def toLowerCase(self, s: str) -> str:
        lower = ''

        for char in s:
            if 'A' <= char <= 'Z':
                lower += chr(ord(char) - ord('A') + ord('a'))
            else:
                lower += char

        return lower
