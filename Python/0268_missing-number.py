class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sequence_sum = (n ** 2 + n) // 2

        return sequence_sum - sum(nums)
