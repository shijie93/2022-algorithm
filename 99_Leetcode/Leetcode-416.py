from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1 == 1:
            return False
        total //= 2
        length = len(nums)
        
        # 判断从 nums 取出若干数量的数字，能否刚好组成和为 total 的子序列
        dp = [[False] * (total + 1) for _ in range(length + 1)]

        for i in range(length + 1):
            dp[i][0] = True

        for i in range(1,  length + 1):
            for j in range(1, total + 1):
                if j - nums[i - 1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] | dp[i-1][j-nums[i-1]]
        
        return dp[length][total]