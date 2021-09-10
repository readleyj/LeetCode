class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first_max, first_max_idx = -1, -1
        second_max = -1

        for idx, num in enumerate(nums):
            if num > first_max:
                first_max, first_max_idx = num, idx

        for idx, num in enumerate(nums):
            if num > second_max and idx != first_max_idx:
                second_max = num

        return (first_max - 1) * (second_max - 1)
