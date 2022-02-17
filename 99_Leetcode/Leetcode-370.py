class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # 利用差分数组进行区间增减
        nums = [0 for _ in range(length)]

        # 得出当前的查分数组
        diff = [0 for _ in range(length)]
        diff[0] = nums[0]

        for i in range(1, length):
            diff[i] = nums[i] - nums[i - 1]