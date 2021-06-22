class Solution:
    def sum_digits(self, num):
        digit_sum = 0

        while num:
            digit_sum += num % 10
            num //= 10

        return digit_sum

    def addDigits(self, num: int) -> int:
        while num // 10:
            num = self.sum_digits(num)

        return num
