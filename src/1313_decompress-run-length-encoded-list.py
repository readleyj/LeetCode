class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        output = []

        for idx in range(1, len(nums), 2):
            freq, val = nums[idx - 1], nums[idx]
            output += freq * [val]

        return output
