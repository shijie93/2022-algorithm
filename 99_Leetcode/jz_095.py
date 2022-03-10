class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        输入：text1 = "abcde", text2 = "ace" 
        输出：3  
        解释：最长公共子序列是 "ace" ，它的长度为 3 。"""

        m, n = len(text1), len(text2)

        # dp[m][n] 为 [0,m], [0,n] 的最长公共子序列的长度

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # base case
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(
                        dp[i-1][j],
                        dp[i][j-1],
                        dp[i-1][j-1])

        return dp[m][n]
