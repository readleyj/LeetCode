class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row_num, col_num = len(matrix), len(matrix[0])

        for row_idx in range(1, row_num):
            for col_idx in range(1, col_num):
                if matrix[row_idx][col_idx] != matrix[row_idx - 1][col_idx - 1]:
                    return False

        return True
