# Problem: Smallest Even Multiple - https://leetcode.com/problems/smallest-even-multiple/

class Solution(object):
    def smallestEvenMultiple(self, n):
        if n % 2 == 0:
            return n
        else:
            return n * 2
        """
        :type n: int
        :rtype: int
        """
        