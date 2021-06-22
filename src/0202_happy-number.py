class Solution:
    def sum_digit_squares(self, n):
        digit_square_sum = 0

        while n:
            digit_square_sum += (n % 10) ** 2
            n //= 10

        return digit_square_sum

    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            digit_square_sum = self.sum_digit_squares(n)

            if digit_square_sum in seen:
                return False

            seen.add(digit_square_sum)
            n = digit_square_sum

        return True
