class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """dp 数组"""
        # 定义：s1[0..i-1] 和 s2[0..j-1] 的 lcs 长度为 dp[i][j]
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[m][n]



    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     """dp 函数"""

    #     memo = [[-1] * len(text2) for _ in range(len(text1))]

    #     def dp(str1, start1, str2, start2):
    #         if start1 == len(str1)or start2 == len(str2):
    #             return 0
            
    #         if memo[start1][start2] != -1:
    #             return memo[start1][start2]
            
    #         if str1[start1] == str2[start2]:
    #             memo[start1][start2] =  1 + dp(str1, start1 + 1, str2, start2 + 1)
    #         else:
    #             memo[start1][start2] =  max(
    #                 dp(str1, start1, str2, start2 + 1),
    #                 dp(str1, start1 + 1, str2, start2)
    #             )
    #         return memo[start1][start2]
        
    #     return dp(text1, 0, text2, 0)