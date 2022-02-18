class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # 利用差分数组进行区间增减
        nums = [0 for _ in range(length)]

        # 得出当前的查分数组
        diff = [0 for _ in range(length)]
        diff[0] = nums[0]
        for i in range(1, length):
            diff[i] = nums[i] - nums[i - 1]

        # 进行操作
        for update in updates:
            start, end, inc = update
            diff[start] += inc
            if (end + 1) < length:
                diff[end + 1] -= inc
        
        # 还原原始的数组
        nums[0] = diff[0]
        for i in range(1, length):
            nums[i] = diff[i] + nums[i - 1]

        return nums