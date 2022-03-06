import pprint
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[10e7] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == 1 and j == 1:
                    dp[i][j] = grid[i - 1][j - 1]
                    continue
                dp[i][j] = min(
                    dp[i][j], 
                    grid[i - 1][j - 1] + dp[i-1][j] if i - 1 >=0 else 10e7,
                    grid[i - 1][j - 1] + dp[i][j-1] if j - 1 >=0 else 10e7
                )
        return dp[m][n]