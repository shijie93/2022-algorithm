from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 先找到最左，然后向右找

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        if left >= len(nums) or nums[left] != target:
            res = [-1, -1]
        else:
            res = [left]
            left += 1
            while left < len(nums):
                if nums[left] == target:
                    left += 1
                    continue
                else:
                    break
            left -= 1
            res.append(left)
        return res
