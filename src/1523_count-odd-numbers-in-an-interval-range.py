class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low + int(high % 2 == 1) + int(low % 2 == 1)) // 2
