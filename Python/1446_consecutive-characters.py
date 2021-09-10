class Solution:
    def maxPower(self, s: str) -> int:
        cur_char, max_power, running_power = '.', -1, 0

        for char in s + '.':
            if char != cur_char:
                cur_char = char
                max_power = max(running_power, max_power)
                running_power = 1
            else:
                running_power += 1

        return max_power
