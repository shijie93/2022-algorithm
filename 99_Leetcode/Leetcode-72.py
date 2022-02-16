class Solution:

    def minDistance(self, s1: str, s2: str) -> int:
        """dp 数组"""
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(n + 1):
            dp[0][i] = i
        for i in range(m + 1):
            dp[i][0] = i
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i-1][j] + 1,
                        dp[i][j-1] + 1,
                        dp[i-1][j-1] + 1
                    )
        return dp[m][n]


    # def minDistance(self, s1: str, s2: str) -> int:
    #     memo = dict() # 备忘录
    #     def dp(i, j):
    #         if i == -1: return j + 1
    #         if j == -1: return i + 1

    #         if (i, j) in memo: 
    #             return memo[(i, j)]
            
    #         if s1[i] == s2[j]:
    #             memo[(i, j)] = dp(i-1, j-1)
    #         else:
    #             memo[(i, j)] = min(
    #                 dp(i-1, j) + 1,
    #                 dp(i, j-1) + 1,
    #                 dp(i-1, j-1) + 1
    #             )
    #         return memo[(i, j)]

    #     return dp(len(s1) - 1, len(s2) - 1)