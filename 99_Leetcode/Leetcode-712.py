from re import L


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        memo = [[-1] * len(s2) for _ in range(len(s1))]

        def dp(str1, start1, str2, start2):
            res = 0

            if start1 == len(str1):
                for i in range(start2, len(str2)):
                    res += ord(str2[i])
                return res

            if start2 == len(str2):
                for i in range(start1, len(str1)):
                    res += ord(str1[i])
                return res
            
            if memo[start1][start2] != -1:
                return memo[start1][start2]
            
            if str1[start1] == str2[start2]:
                memo[start1][start2] =  dp(str1, start1 + 1, str2, start2 + 1)
            else:
                memo[start1][start2] =  min(
                    ord(str2[start2]) + dp(str1, start1, str2, start2 + 1),
                    ord(str1[start1]) + dp(str1, start1 + 1, str2, start2)
                )
            return memo[start1][start2]

        return dp(s1, 0, s2, 0)