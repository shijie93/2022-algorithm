class Solution:
    def isValid(self, s: str) -> bool:
        
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