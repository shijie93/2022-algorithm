class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 投票算法
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate
