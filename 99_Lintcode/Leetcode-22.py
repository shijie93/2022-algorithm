from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        def _gen(left, right, n, result):
            if left > n or right > n:
                return

            if left == n and right == n:
                self.result.append(result)
            
            if left < n: _gen(left + 1, right, n, result + "(")
            if left > right and right < n: _gen(right + 1, right, n, result + ")")
        
        _gen(0, 0, n // 2, "")

        return self.result