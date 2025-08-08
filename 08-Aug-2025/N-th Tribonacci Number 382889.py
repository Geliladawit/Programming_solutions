# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        T = [0, 1, 1]
        if n == 0:
            return 0
        for i in range(2,n):
            T.append(T[i] + T[i-1] + T[i-2])
        return T[-1]