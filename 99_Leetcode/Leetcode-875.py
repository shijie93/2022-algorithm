from cmath import pi
import plistlib


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """输入: piles = [3,6,7,11], H = 8
           输出: 4
        """

        def f(piles, x):
            hour = 0
            for p in piles:
                hour += p // x
                if p % x > 0:
                    hour += 1
            return hour
        
        left = 1
        right = int(1e9)

        while left <= right:

            mid = left + (right - left) // 2

            ret = f(piles, mid)
            if ret < h:
                right = mid - 1
            elif ret > h:
                left = mid + 1
            elif ret == h:
                right = mid - 1
        
        return left
