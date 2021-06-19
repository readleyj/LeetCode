class Solution:
    SENTINEL = -1e5

    def removeDuplicates(self, nums: List[int]) -> int:
        prev_num = self.SENTINEL

        for idx, num in enumerate(nums):
            if num == prev_num:
                nums[idx] = self.SENTINEL

            prev_num = num

        curr_idx = 0

        for idx, num in enumerate(nums):
            if num != self.SENTINEL:
                nums[curr_idx] = num
                curr_idx += 1

        return curr_idx
