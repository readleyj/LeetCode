class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        char_diff = Counter(t) - Counter(s)

        return list(char_diff.keys())[0]
