class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        curr_idx = len(digits) - 1

        while True:
            if digits[curr_idx] + 1 != 10:
                digits[curr_idx] += 1
                break

            digits[curr_idx] = 0
            curr_idx -= 1

            if curr_idx == -1:
                return [1] + digits

        return digits
