class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = 0

        while x or y:
            result += (x & 1 != y & 1)
            x, y = x >> 1, y >> 1

        return result
