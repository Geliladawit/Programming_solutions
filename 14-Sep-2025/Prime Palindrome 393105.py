# Problem: Prime Palindrome - https://leetcode.com/problems/prime-palindrome/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(x):
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            r = int(x**0.5)
            for i in range(3, r + 1, 2):
                if x % i == 0:
                    return False
            return True

        def generate_palindromes(limit):
            for length in range(1, limit + 1):
                start = 10**(length - 1)
                end = 10**length
                for half in range(start, end):
                    s = str(half)
                    pal = int(s + s[-2::-1])
                    yield pal

        if n <= 2:
            return 2
        if n <= 3:
            return 3
        if n <= 5:
            return 5
        if n <= 7:
            return 7
        if n <= 11:
            return 11

        for pal in generate_palindromes(6):
            if pal >= n and is_prime(pal):
                return pal
