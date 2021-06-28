class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected_heights, num_diff = sorted(heights), 0

        for height, expected in zip(heights, expected_heights):
            num_diff += height != expected

        return num_diff
