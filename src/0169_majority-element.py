class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        stack = []

        for num in nums:
            if not stack or stack[-1] == num:
                stack.append(num)
            else:
                stack.pop()

        return stack[-1]
