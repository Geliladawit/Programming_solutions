# Problem: Distinct Prime Factors of Product of Array - https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def prime_factor(n):
            factors = []
            while n % 2 == 0:
                factors.append(2)
                n //= 2
            
            for i in range(3, int(n**0.5) + 1, 2):
                while n % i == 0:
                    factors.append(i)
                    n //= i
                    
            if n > 2:
                factors.append(n)
            
            return factors
        res = []
        for n in nums:
            res += prime_factor(n)
        return len(Counter(res))