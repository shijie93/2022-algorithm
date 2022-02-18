import collections

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """输入: s = "cbaebabacd", p = "abc"
输出: [0,6]"""

        m, n = len(s), len(p)
        need = collections.defaultdict(int)

        for c in p: need[c] += 1

        left = right = valid = 0
        win = collections.defaultdict(int)
        res = set()
        while right < m:
            c = s[right]
            right += 1

            if c in need:
                win[c] += 1
                if win[c] == need[c]:
                    valid += 1
            
            while right - left >= n:
                if valid == len(need):
                    res.add(left)
                
                d = s[left]
                left += 1

                if d in need:
                    if win[d] == need[d]:
                        valid -= 1
                    win[d] -= 1
        return list(res)

