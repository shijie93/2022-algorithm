class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        输入：nums = [1,1,2]
        输出：2, nums = [1,2,_]
        '''

        # 题目要求原地

        n = len(nums)

        p1, p2 = 0, 0

        while p1 < n and p2 < n and p1 <= p2:
            if nums[p1] != nums[p2]:
                p1 += 1
                nums[p1], nums[p2] = nums[p2], nums[p1]
            p2 += 1
        
        return p1 + 1