class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            s1 = self.getPalindromic(s, i, i)
            s2 = self.getPalindromic(s, i, i+1)
            
            res = s1 if len(s1) > len(res) else res
            res = s2 if len(s2) > len(res) else res
        
        return res
    
    def getPalindromic(self, s, l, r):
        # 返回以 s[l] 为中心的回文子串
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]