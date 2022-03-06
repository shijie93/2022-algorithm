class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
            输入：nums = [3,2,2,3], val = 3
            输出：2, nums = [2,2]
        """
        m = len(nums)
        slow = fast = 0

        while fast < m:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow