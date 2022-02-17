from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.presSum = [0 for _ in range(len(nums) + 1)]
        for i in range(1, len(self.nums) + 1):
            self.presSum[i] = self.presSum[i - 1] + nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        return self.presSum[right + 1] - self.presSum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)