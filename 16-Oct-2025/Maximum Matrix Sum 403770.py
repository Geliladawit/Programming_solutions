# Problem: Maximum Matrix Sum - https://leetcode.com/problems/maximum-matrix-sum/description/?envType=problem-list-v2&envId=matrix

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ans = 0
        neg = 0
        mat_min = float("inf")
        for row in matrix:
            for n in row:
                ans += abs(n)
                mat_min = min(mat_min, abs(n))
                if n < 0:
                    neg += 1

        if neg & 1:
            ans -= 2 * mat_min
        return ans