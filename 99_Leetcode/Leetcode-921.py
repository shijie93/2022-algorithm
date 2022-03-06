class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack = []
        ret = 0
        for c in s:
            if c == '(':
                stack.append(c)
            elif not stack or (stack[-1] != '('):
                ret += 1
            else:
                stack.pop()
        if stack: ret += len(stack)
        return ret