class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n: return 1

        # 如果 n 是负数，转变为正数的导数
        if n < 0: return 1 / self.myPow(x, -n)

        # 如果 n 是奇数，拆分成 x * 偶数
        if n % 2: return x * self.myPow(x, n-1)

        # 分治
        return self.myPow(x*x, n/2)

"""class Solution:
    # 位运算
    def myPow(self, x: float, n: int) -> float:
        if not n: return 1
        if n < 0:
            x = 1 / x
            n = -n
        
        ret = 1
        while n > 0:
            if n & 1:
                ret *= x
            x *= x
            n >>= 1

        return ret"""