from typing import List
import numpy as np

class Solution:
    """
        输入 [7,1,5,3,6,4]
        输出 5 (1, 6)
    """
    def maxProfit(self, prices: List[int]) -> int:

        # dp[days][k][0 or 1] 代表在某一天 买入或者卖出所获得的收益

        dp = np.zeros((len(prices),  2), dtype='int64')

        for i in range(len(prices)):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue

            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], -prices[i])

        return int(dp[len(prices) - 1][0])