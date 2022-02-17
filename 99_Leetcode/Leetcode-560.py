class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        import collections
        memo = collections.defaultdict(int)
        memo[0] = 1

        res = sum_i = 0

        for i in range(len(nums)):
            sum_i += nums[i]

            sum_j = sum_i - k
            if sum_j in memo:
                res += memo[sum_j]
            
            memo[sum_i] += 1
        
        return res