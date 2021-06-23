class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = [word for word in s.split(' ') if word]

        if not words:
            return 0

        return len(words[-1])
