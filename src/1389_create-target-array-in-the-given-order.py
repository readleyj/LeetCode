class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []

        for idx in range(len(nums)):
            result.insert(index[idx], nums[idx])

        return result
