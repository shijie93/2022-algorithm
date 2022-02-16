class Solution:
    """给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。"""
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0

        max_len = 0
        win = []
        while left <= right and right < len(s):
            
            new_val = s[right]

            if new_val not in win:
                win.append(new_val)
                right += 1
            else:
                win.pop(0)
                left += 1
            
            max_len = max(max_len, len(win))
        return max_len