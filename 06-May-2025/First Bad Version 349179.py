# Problem: First Bad Version - https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        while start <= n:
            bad = (start+n)//2
            res = isBadVersion(bad)
            if not res:
                start = bad +1
            elif res and isBadVersion(bad-1):
                n = bad - 1
            else:
                return bad