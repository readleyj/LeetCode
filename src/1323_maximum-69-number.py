class Solution:
    def maximum69Number(self, num: int) -> int:
        result = num

        num_str = str(num)

        for idx, char in enumerate(num_str):
            if char == '6':
                result += 3 * pow(10, len(num_str) - idx - 1)
                break

        return result
