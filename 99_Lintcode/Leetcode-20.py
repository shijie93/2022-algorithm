class Solution:
    def isValid(self, s: str) -> bool:
        
        # 32 ms
        # 14.9 MB
        stack = []
        match = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }

        for i in s:
            if i in match.values():
                stack.append(i)
            elif i in match and (len(stack) == 0 or stack[-1] != match[i]):
                return False
            else:
                stack.pop()
        
        return len(stack) == 0