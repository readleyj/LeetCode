class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        num_occurences = Counter(nums)

        total = 0
        for num in nums:
            if num_occurences[num] == 1:
                total += num

        return total
