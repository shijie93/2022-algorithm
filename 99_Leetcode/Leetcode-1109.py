class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:

        # 利用差分数组进行区间增减
        nums = [0 for _ in range(n)]

        # 得出当前的查分数组
        diff = [0 for _ in range(n)]
        diff[0] = nums[0]
        for i in range(1, n):
            diff[i] = nums[i] - nums[i - 1]

        # 进行操作
        for booking in bookings:
            start, end, inc = booking
            diff[start - 1] += inc
            if (end - 1 + 1) < n:
                diff[end - 1 + 1] -= inc
        
        # 还原原始的数组
        nums[0] = diff[0]
        for i in range(1, n):
            nums[i] = diff[i] + nums[i - 1]

        return nums