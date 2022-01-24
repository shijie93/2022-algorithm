class Solution:
    """
    @param s: string s
    @param t: string t
    @return: Given two strings s and t, write a function to determine if t is an anagram of s.
    """
    def isAnagram(self, s, t):
        # write your code here
        if len(s) != len(t):
            return False

        buckets = [0 for _ in range(26)]

        for index in range(len(s)):
            buckets[ord(s[index]) - ord('a')] += 1
            buckets[ord(t[index]) - ord('a')] -= 1

        if buckets.count(0) == len(buckets):
            return True
        return False

if __name__ == '__main__':
    s = Solution()

    print(s.isAnagram("anagram", "nagaram"))
    print(s.isAnagram("car", "rat"))