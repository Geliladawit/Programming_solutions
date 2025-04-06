# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        n = len(intervals)
        if n == 1 and intervals[0][0] != intervals[0][1]:
            return [-1]
        elif n == 1 and intervals[0][0] == intervals[0][1]:
            return [0]
        ans = [-1] * n
        start_map = {}
        for i in range(n):
            start_map[intervals[i][0]] = i
        sorted_starts = sorted(start_map.keys())
        for i in range(n):
            end = intervals[i][1]
            for start in sorted_starts:
                if start >= end:
                    ans[i] = start_map[start]
                    break
        return ans