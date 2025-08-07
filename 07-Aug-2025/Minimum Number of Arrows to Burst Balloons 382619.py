# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        print(points)
        left = 0
        count = 0
        while left < len(points):
            count += 1
            current_end = points[left][1]
            while left < len(points) and points[left][0] <= current_end:
                left += 1

        return count
