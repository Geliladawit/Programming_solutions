# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int = {"I": 1, "V": 5, "X": 10, "L":50, "C": 100, "D": 500, "M":1000}
        ans = 0
        prev = 0
        for char in reversed(s):
            curr = roman_int[char]
            if curr< prev:
                ans -= curr
            else:
                ans += curr
            prev = curr
        return ans