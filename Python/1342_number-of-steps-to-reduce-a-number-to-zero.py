class Solution:
    def numberOfSteps(self, num: int) -> int:
        num_steps = 0

        while num:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1

            num_steps += 1

        return num_steps
