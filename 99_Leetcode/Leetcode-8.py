import re
class Solution:
    def myAtoi(self, s: str) -> int:
        return max(min(int(re.findall('^[\+\-]?\d+', s.strip())[0]), 2**31 - 1), -2**31)

if __name__ == '__main__':

    s = Solution()
    assert s.myAtoi("42") == 42
    assert s.myAtoi("   -42") == -42
    assert s.myAtoi("4193 with words") == 4193