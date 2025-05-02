# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        modulo = 10**9 + 7
        no_fours = n//2
        no_fives = n - no_fours

        def pow(x,n,modulo):
            if n == 0:
                return 1 

            if n % 2 == 0:
                half = pow(x,n // 2,modulo)
                return (half * half) % modulo 

            return (x * pow(x,n - 1,modulo)) % modulo


        return (pow(5,no_fives,modulo) * pow(4,no_fours,modulo)) % modulo
