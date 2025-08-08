# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix[0])
        for row in range(n - 2, -1, -1):
            for col in range(n):
                left = matrix[row + 1][col - 1] if col > 0 else float('inf')
                down = matrix[row + 1][col]
                right = matrix[row + 1][col + 1] if col < n - 1 else float('inf')
                
                matrix[row][col] += min(left, down, right)
        
        return min(matrix[0])
                