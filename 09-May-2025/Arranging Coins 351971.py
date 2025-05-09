# Problem: Arranging Coins - https://leetcode.com/problems/arranging-coins/description/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        stair = 0
        c = 0
        while n >= c:
            stair += 1
            c += stair
        if n == c:
            return stair
        else:
            return stair - 1