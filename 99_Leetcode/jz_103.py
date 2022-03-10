class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        输入：coins = [1, 2, 5], amount = 11
        输出：3 
        解释：11 = 5 + 5 + 1"""

        # dp[amount] 表示凑成amount所需要的硬币数
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i - coin] + 1, dp[i])
        return dp[amount] if dp[amount] != amount + 1 else -1
