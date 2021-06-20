class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char_counts = Counter(text)

        char_counts['l'] //= 2
        char_counts['o'] //= 2

        return min([char_counts[char] for char in 'balloon'])
