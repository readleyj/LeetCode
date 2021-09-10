class Solution:
    def shift(self, char, offset):
        return chr(ord(char) + offset)

    def replaceDigits(self, s: str) -> str:
        result = ''

        for idx in range(len(s)):
            if idx % 2 == 1:
                result += self.shift(s[idx - 1], int(s[idx]))
            else:
                result += s[idx]

        return result
