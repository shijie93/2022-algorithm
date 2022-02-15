from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 最长递增子序列
        # 定义 dp 数组表示以 nums[i] 为结尾的子序列的最长递增序列的长度

        length = len(nums)

        dp = [1 for i in range(length)]

        for i in range(length):
            for j in range(0, i + 1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        
        return max(dp)