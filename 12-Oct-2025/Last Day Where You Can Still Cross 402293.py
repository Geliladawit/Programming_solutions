# Problem: Last Day Where You Can Still Cross - https://leetcode.com/problems/last-day-where-you-can-still-cross/

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        total = row * col
        top, bottom = total, total + 1   
        uf = UnionFind(total + 2)
        grid = [[0] * col for _ in range(row)]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def cell_id(r, c):
            return r * col + c

        for day in range(len(cells) - 1, -1, -1):
            r, c = cells[day]
            r -= 1
            c -= 1
            grid[r][c] = 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                    uf.union(cell_id(r, c), cell_id(nr, nc))

            if r == 0:
                uf.union(cell_id(r, c), top)
            if r == row - 1:
                uf.union(cell_id(r, c), bottom)

            if uf.connected(top, bottom):
                return day

        return 0
