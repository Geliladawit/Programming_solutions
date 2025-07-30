# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        memory = defaultdict(int)
        def fib(i):
            if i == 1 or i == 0:
                return 1
            if i not in memory:
                memory[i] = fib(i-1) + fib(i - 2) 
            return memory[i] 
        return fib(n) 