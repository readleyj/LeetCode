class Solution:
    def compute_digit_sum_prod(self, n):
        digit_sum, digit_prod = 0, 1

        while n:
            digit = n % 10
            digit_sum, digit_prod = digit_sum + digit, digit_prod * digit

            n = n // 10

        return digit_sum, digit_prod

    def subtractProductAndSum(self, n: int) -> int:
        digit_sum, digit_prod = self.compute_digit_sum_prod(n)

        return digit_prod - digit_sum
