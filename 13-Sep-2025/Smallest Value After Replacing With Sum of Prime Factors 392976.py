# Problem: Smallest Value After Replacing With Sum of Prime Factors - https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution:
    def smallestValue(self, n: int) -> int:
        def replace(n):
            factors = []
            temp = n
            while temp % 2 == 0:
                factors.append(2)
                temp //= 2
            for i in range(3, int(temp**0.5) + 1, 2):
                while temp % i == 0:
                    factors.append(i)
                    temp //= i
            if temp > 2:
                factors.append(temp)

            s = sum(factors)
            if s == n:   
                return n
            return replace(s)

        return replace(n)