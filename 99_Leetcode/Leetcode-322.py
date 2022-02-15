from typing import List

class Solution:
    """
    给你一个整数数组 coins ,表示不同面额的硬币;以及一个整数 amount ,表示总金额。
    计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额,返回 -1 。
    你可以认为每种硬币的数量是无限的。

    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        """dp 数组"""

        # 初始化 dp 数组
        dp = [amount + 1 for _ in range(amount + 1)]

        # base case
        dp[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                if i - coin < 0: continue
                dp[i] = min(dp[i], 1 + dp[i - coin])

        return -1 if dp[amount] == amount + 1 else dp[amount]
    
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     """dp 函数"""
    #     memo = dict()
    #     def dp(n):
    #         if n == 0: return 0
    #         if n < 0: return -1

    #         if n in memo:
    #             return memo[n]

    #         res = float('inf')
    #         for coin in coins:
    #             sub = dp(n - coin)
    #             if sub == -1: continue
    #             res = min(res, 1 + sub)

    #         memo[n] = res if res != float('inf') else -1
    #         return memo[n]
        
    #     return dp(amount)
            
