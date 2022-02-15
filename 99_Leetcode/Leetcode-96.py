from functools import lru_cache

class Solution:
    def numTrees(self, n: int) -> int:
        return self.count(1, n)
    
    @lru_cache
    def count(self, left, right):

        if left > right:
            return 1

        res = 0
        for i in range(left, right + 1):
            le = self.count(left, i-1)
            ri = self.count(i+1, right)
            res += le * ri
        
        return res