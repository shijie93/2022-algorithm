import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = []
        for num in nums:
            if len(self.nums) < self.k:
                heapq.heappush(self.nums, num)
            else:
                if num > self.nums[0]:
                    heapq.heappushpop(self.nums, num)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        else:
            if val > self.nums[0]:
                heapq.heappushpop(self.nums, val)
        return self.nums[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)