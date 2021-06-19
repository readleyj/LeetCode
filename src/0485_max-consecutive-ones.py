class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        running_count, max_count = 0, -1

        for num in nums + [0]:
            max_count = max(running_count, max_count)

            if num == 0:
                running_count = 0
            else:
                running_count += 1

        return max_count
