class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = Counter(nums)
        total = 0

        for count in counter.values():
            total += (count * (count - 1)) // 2

        return total
