class Solution:
    def reverse_num(self, num):
        digits = []

        while num:
            digits.append(num % 10)
            num //= 10

        return sum(digit * pow(10, len(digits) - idx - 1) for idx, digit in enumerate(digits))

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        return x == self.reverse_num(x)
        s
