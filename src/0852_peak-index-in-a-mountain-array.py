class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        prev_idx, prev_num = -1, -1

        for idx, num in enumerate(arr):
            if num < prev_num:
                break

            prev_idx, prev_num = idx, num

        return prev_idx
