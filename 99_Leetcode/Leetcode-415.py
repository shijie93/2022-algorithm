from re import M


import collections
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n, m = len(num1), len(num2)
        if n < m:
            num1 = '0' * (m - n) + num1
            total = m
        else:
            num2 = '0' * (n - m) + num2
            total = n
            
        cur1 = cur2 = total - 1
        res = collections.deque()
        up = 0
        while cur1 >= 0 and cur2 >= 0:
            c1, c2 = num1[cur1], num2[cur2]

            tmp = int(c1) + int(c2) + up
            res.appendleft(str(tmp % 10))
            up = tmp // 10

            cur1 -= 1
            cur2 -= 1
        
        if up > 0:
            res.appendleft(str(up))
        
        res = ''.join(res)
        return res


if __name__ == '__main__':
    s = Solution()

    assert s.addStrings('11', '123') == '134'
    assert s.addStrings('456', '77') == '533'
    assert s.addStrings('0', '0') == '0'