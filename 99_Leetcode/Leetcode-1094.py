class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        n = 1000

        # 利用差分数组进行区间增减
        nums = [0 for _ in range(n)]

        # 得出当前的查分数组
        diff = [0 for _ in range(n)]
        diff[0] = nums[0]
        for i in range(1, n):
            diff[i] = nums[i] - nums[i - 1]

        # 进行操作
        for trip in trips:
            inc, start, end  = trip
            diff[start] += inc
            if (end + 1) < n:
                diff[end] -= inc
        
        # 还原原始的数组
        nums[0] = diff[0]
        if nums[0] > capacity: return False
        for i in range(1, n):
            nums[i] = diff[i] + nums[i - 1]
            if nums[i] > capacity:
                return False
        return True
 