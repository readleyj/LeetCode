class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequencies = Counter(nums)

        return sorted(nums, key=lambda num: (frequencies[num], -num))
