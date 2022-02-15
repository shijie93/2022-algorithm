class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n & (n - 1) == 0 and n != 0