# Problem: Knight Probability in Chessboard - https://leetcode.com/problems/knight-probability-in-chessboard/

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
        memo = {}

        def dfs(moves_left, r, c):
            if r < 0 or r >= n or c < 0 or c >= n:
                return 0
            if moves_left == 0:
                return 1
            if (moves_left, r, c) in memo:
                return memo[(moves_left, r, c)]
            prob = 0
            for dr, dc in moves:
                prob += dfs(moves_left - 1, r + dr, c + dc) / 8
            memo[(moves_left, r, c)] = prob
            return prob

        return dfs(k, row, column)