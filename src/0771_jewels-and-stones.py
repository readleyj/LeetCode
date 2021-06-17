class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)

        count = 0

        for stone in stones:
            count += stone in jewel_set

        return count
