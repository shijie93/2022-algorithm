from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # 484 ms
        # 15.6 MB
        # for index, val in enumerate(nums):
        #     if target - val in nums[index + 1:]:
        #         return index, nums[index + 1:].index(target - val) + index + 1


        # 48 ms
        # 16 MB
        cache = dict()
        for index, val in enumerate(nums):
            if val not in cache:
                cache[val] = index

            if target - val in cache and cache[target - val] != index:
                return [cache[target - val], index]