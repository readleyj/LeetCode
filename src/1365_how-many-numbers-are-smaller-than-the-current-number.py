class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        mapper = dict()

        for idx, num in enumerate(sorted_nums):
            if num not in mapper:
                mapper[num] = idx

        return [mapper[num] for num in nums]
