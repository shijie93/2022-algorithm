import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """输入：s1 = "ab" s2 = "eidbaooo"
            输出：true"""
        m, n = len(s2), len(s1)
        need = collections.defaultdict(int)
        for c in s1: need[c] += 1

        left = right = valid = 0
        win = collections.defaultdict(int)
        while right < m:
            c = s2[right]
            right += 1

            if c in need:
                win[c] += 1
                if win[c] == need[c]:
                    valid += 1

            # 因为要求是 s1 排列的子串，所以窗口缩小的条件是窗口大小大于了 s1 的长度
            while right - left >= n:
                # 符合条件
                if valid == len(need):
                    return True
                
                # 更新 left
                d = s2[left]
                left += 1
                if d in need:
                    if win[d] == need[d]:
                        valid -= 1
                    win[d] -= 1
        return False

            

            
