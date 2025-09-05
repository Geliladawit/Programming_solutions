# Problem: Count Servers that Communicate - https://leetcode.com/problems/count-servers-that-communicate/description/

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid[0])
        n = len(grid)
        r_c, c_c =0, 0
        col_count = [0] * m
        row_count = [0] * n
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (row_count[i] > 1 or col_count[j] > 1):
                    res += 1
            
        return res