class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        differences = []

        for x, y in zip(nums[0::], nums[1::]):
            differences.append(y - x)

        return all(diff <= 0 for diff in differences) or all(diff >= 0 for diff in differences)
