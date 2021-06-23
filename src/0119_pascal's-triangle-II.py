class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev_row = [1]

        for idx in range(1, rowIndex + 1):
            cur_row = [1] * (idx + 1)

            for i in range(1, idx):
                cur_row[i] = prev_row[i] + prev_row[i - 1]

            prev_row = cur_row

        return prev_row
