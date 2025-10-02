# Problem: Path With Minimum Effort - https://leetcode.com/problems/path-with-minimum-effort/description/

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])

        diff_matrix = [[float('inf')] * col for _ in range(row)]
        diff_matrix[0][0] = 0
        vis = [[False] * col for _ in range(row)]
        q = [(0, 0, 0)]

        while q:
            diff, x,  y = heapq.heappop(q)
            vis[x][y] = True

            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                newX = x + dx
                newY = y + dy

                if 0 <= newX < row and 0 <= newY < col and not vis[newX][newY]:
                    curr_diff = abs(heights[newX][newY] - heights[x][y])
                    mx_diff = max(curr_diff, diff_matrix[x][y])
                    if diff_matrix[newX][newY] > mx_diff:
                        diff_matrix[newX][newY] = mx_diff
                        heapq.heappush(q, (mx_diff,newX,newY))

        return diff_matrix[row - 1][col - 1]
