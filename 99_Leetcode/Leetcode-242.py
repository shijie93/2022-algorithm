from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        flue = defaultdict(int)

        for a, b in zip(s, t):
            flue[a] += 1
            flue[b] -= 1
        
        return all(flue[a] == 0 for a in flue)