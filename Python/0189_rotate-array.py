class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        to_rotate = k % len(nums)
        nums.reverse()

        nums[:to_rotate] = reversed(nums[:to_rotate])
        nums[to_rotate:] = reversed(nums[to_rotate:])
