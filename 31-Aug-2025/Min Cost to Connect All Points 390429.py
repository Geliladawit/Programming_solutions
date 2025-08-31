# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        result = 0
        visited = set()
        minHeap = [(0, 0)]  

        while len(visited) < n:
            cost, i = heapq.heappop(minHeap)
            if i in visited:
                continue
            visited.add(i)
            result += cost

            for j in range(n):
                if j not in visited:
                    dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    heapq.heappush(minHeap, (dist, j))

        return result
