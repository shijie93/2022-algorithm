from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 动态规划，使用 dp 数组维护状态
        # dp[i][j] 保存的是只使用前i个物品，塞满背包为 j 的背包的方法
        # base dp[i][0] = 1，其他为0
        # 每个物品存在放与不妨两种情况

        n = len(coins)

        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1

        
        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if j - coins[i - 1] >= 0:
                    # 每一个位置的可能性总和 = 不放 + 放
                    dp[i][j] = dp[i-1][j] + dp[i][j - coins[i-1]]
                else:
                    # 不放
                    dp[i][j] = dp[i-1][j]

        return dp[n][amount]