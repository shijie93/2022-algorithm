from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        if not nums: return []

        result = []
        win = []
        for index, val in enumerate(nums):

            # 右移窗口
            if index >= k and win[0] <= index - k:
                win.pop(0)
            
            # 移除比 val 小的下标
            while win and nums[win[-1]] <= val:
                win.pop()
        
            # 加入 val 下标
            win.append(index)

            # 追加到结果中
            if index >= k-1:
                result.append(nums[win[0]])
        return result
