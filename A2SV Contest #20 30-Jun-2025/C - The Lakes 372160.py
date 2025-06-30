# Problem: C - The Lakes - https://codeforces.com/gym/618729/problem/C

def solve ():
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid. append (row)
    visited = [[False] *m for _ in range(n)]
    max_volume = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    def dfs_iterative(start_i, start_j):
        stack = [(start_i, start_j)]
        volume = 0
        while stack:
            i, j= stack.pop()
            if i < 0 or i >= n or j< 0 or j >=m or visited[i][j] or grid[i][j] == 0:
                continue
            visited[i][j] = True
            volume += grid[i][j]
            for di, dj in directions:
                stack. append ((i + di, j + dj))
        return volume
    for i in range(n) :
        for j in range(m) :
            if not visited[i][j] and grid[i][j] > 0:
                lake_volume = dfs_iterative(i, j)
                max_volume = max (max_volume, lake_volume)
    print (max_volume)
t = int(input())
for _ in range(t):
    solve()