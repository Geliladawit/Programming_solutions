# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [True] * (n + 1)
        p = 2

        while p * p <= n:
            if prime[p]:
                
                for i in range(p * p, n, p):
                    prime[i] = False
            p += 1

        res = []
        for p in range(2, n):
            if prime[p]:
                res.append(p)
        
        return len(res)