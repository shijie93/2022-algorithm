class Solution:
    def fib(self, n: int) -> int:
        if n < 2: return n
        ppre, pre = 0, 1
        for i in range(2, n + 1):
            res = ppre + pre
            ppre, pre = pre, res
        return res