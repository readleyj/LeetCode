class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        curr_idx = 0

        for num in nums:
            if num != 0:
                nums[curr_idx] = num
                curr_idx += 1

        nums[curr_idx:] = (len(nums) - curr_idx) * [0]
