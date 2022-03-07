class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        输入: s = "abcabcbb"
        输出: 3 
        '''
        need = dict()
        left = right = l = res = 0
        while left <= right and right < len(s):
            new_char = s[right]

            if new_char not in need:
                need[new_char] = 1
                l += 1
                right += 1
            else:
                del need[s[left]]
                l -= 1
                left += 1

            res = max(res, l)
            print(need)
        return res
        