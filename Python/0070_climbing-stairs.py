class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1] * (n + 1)

        for num in range(2, n + 1):
            dp[num] = dp[num - 1] + dp[num - 2]

        return dp[n]
