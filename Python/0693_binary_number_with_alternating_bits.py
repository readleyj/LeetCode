class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        last_bit = -1

        while n:
            curr_bit = n & 1

            if last_bit != -1 and curr_bit == last_bit:
                return False

            last_bit = curr_bit

            n >>= 1

        return True
