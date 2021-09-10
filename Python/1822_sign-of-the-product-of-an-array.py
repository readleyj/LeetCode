class Solution:
    def arraySign(self, nums: List[int]) -> int:
        num_negative = 0

        for num in nums:
            if num == 0:
                return 0

            num_negative += (num < 0)

        return -1 if num_negative % 2 else 1
