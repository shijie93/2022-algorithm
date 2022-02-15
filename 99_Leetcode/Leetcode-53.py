from typing import List


class Solution:
    
    def maxSubArray(self, nums: List[int]) -> int:
        # 动态规划
        # dp[i] = dp[i-1] + nums[i]
        dp = nums.copy()
        for i in range(1, len(nums)):
            dp[i] = max(dp[i], dp[i-1] + nums[i])
        return max(dp)