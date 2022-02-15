class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left < right:
            mid = (left + right) // 2
            if mid * mid < x: left = mid + 1
            elif mid * mid > x: right = mid - 1
            else: return mid
        return left if left * left <= x else left - 1
                