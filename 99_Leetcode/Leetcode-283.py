class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # left -> 调整好的的数组后一位（为0）
        # right -> 未调整的数组第一位
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1