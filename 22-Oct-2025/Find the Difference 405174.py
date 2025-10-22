# Problem: Find the Difference - https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = Counter(s)
        count_t = Counter(t)
        for i in t:
            if count_t[i] != count_s.get(i,0):
                return i
        