# Problem: 1561. Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/

class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        left = 0
        right = len(piles) - 1
        ans = 0
        piles.sort()
        while left < right:
            ans += piles[right-1]
            right -= 2 
            left += 1
        return ans           