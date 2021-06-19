class Solution:
    def calc_num_digits(self, n):
        num_digits = 0

        while n:
            num_digits += 1
            n //= 10

        return num_digits

    def findNumbers(self, nums: List[int]) -> int:
        count_even = 0

        for num in nums:
            count_even += int(self.calc_num_digits(num) % 2 == 0)

        return count_even
