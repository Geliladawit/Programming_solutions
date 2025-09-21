# Problem: Game of Life - https://leetcode.com/problems/game-of-life/description/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        st = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                s = 0
                if i - 1 >= 0:
                    s += board[i - 1][j]
                if i + 1 < m:
                    s += board[i + 1][j]
                if j - 1 >= 0:
                    s += board[i][j - 1]
                if j + 1 < n:
                    s += board[i][j + 1]
                if i + 1 < m and j + 1 < n:
                    s += board[i + 1][j + 1]
                if i + 1 < m and j - 1 >= 0:
                    s += board[i + 1][j - 1]
                if i - 1 >= 0 and j + 1 < n:
                    s += board[i - 1][j + 1]
                if i - 1 >= 0 and j - 1 >= 0:
                    s += board[i - 1][j - 1]
                if board[i][j] == 1:
                    if s == 2 or s == 3:
                        st[i][j] = 1
                else:
                    if s == 3:
                        st[i][j] = 1
        for i in range(m):
            for j in range(n):
                board[i][j] = st[i][j]