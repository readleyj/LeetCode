class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return sorted(nums, reverse=True, key=lambda num: num % 2 == 0)
