class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        prev_row = [1]

        for idx in range(2, numRows + 1):
            cur_row = [1] * idx

            for i in range(1, idx - 1):
                cur_row[i] = prev_row[i] + prev_row[i - 1]

            prev_row = cur_row
            result.append(cur_row[:])

        return result
