
import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """s = "ADOBECODEBANC", t = "ABC" 输出 "BANC"""
        need = collections.defaultdict(int)
        win = collections.defaultdict(int)

        for c in t:
            need[c] += 1
        
        m, n= len(s), len(need)  
        start = left = right = valid = 0
        min_len = float('inf')

        while right < m:
            c = s[right]
            right += 1

            if c in need:
                # 先更新再判断
                win[c] += 1

                # 首次 c 字符达到约定次数
                if win[c] == need[c]:
                    valid += 1

            # 足够字符
            while valid == n:
                # 首先记录最小子串的 start 和 min_len
                if (right - left) < min_len:
                    start = left
                    min_len = right - left
                
                # 左指针更新
                d = s[left]
                left += 1
                if d in need:

                    # 先判断再更新
                    # d 字符处于不符合要求的临界，只要失去一个就不符合要求
                    if win[d] == need[d]:

                        # 由于 d 已经确定要移除，所以匹配字符-1
                        valid -= 1
                    
                    # 更新
                    win[d] -= 1

        return "" if min_len == float('inf') else s[start:start + min_len]
            