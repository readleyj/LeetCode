class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]

        set_bits = [0 for _ in range(n + 1)]
        set_bits[1] = 1

        last_power_of_two = 1

        for num in range(2, n + 1):
            if num == last_power_of_two * 2:
                set_bits[num] = 1
                last_power_of_two *= 2
                continue

            set_bits[num] = 1 + set_bits[num - last_power_of_two]

        return set_bits
