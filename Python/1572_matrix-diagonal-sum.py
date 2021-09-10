class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        mat_dim = len(mat)
        diag_sum = 0

        for row_idx, col_idx in [(idx, idx) for idx in range(mat_dim)]:
            diag_sum += mat[row_idx][col_idx]
            diag_sum += mat[row_idx][mat_dim - col_idx - 1]

        diag_sum -= (mat_dim % 2 == 1) * (mat[mat_dim // 2][mat_dim // 2])
        return diag_sum
