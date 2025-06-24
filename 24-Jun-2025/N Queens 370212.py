# Problem: N Queens - https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        positive_diag = set()
        negative_diag = set()
        cols = set()
        board = [["."] * n for i in range(n)]
        res = []

        def backtrack(s):
            if s == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for i in range(n):
                if i not in cols and (s+i) not in positive_diag and (s-i) not in negative_diag:
                    cols.add(i)
                    positive_diag.add(s+i)
                    negative_diag.add(s-i)
                    board[s][i] = "Q"

                    backtrack(s+1)

                    cols.remove(i)
                    positive_diag.remove(s+i)
                    negative_diag.remove(s-i)
                    board[s][i] = "."
                else:
                    continue

        backtrack(0)

        return res