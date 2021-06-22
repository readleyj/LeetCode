class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False

        divisors = [2, 3, 5]

        while True:
            for divisor in divisors:
                if n % divisor == 0:
                    n //= divisor
                    break
            else:
                return n == 1
