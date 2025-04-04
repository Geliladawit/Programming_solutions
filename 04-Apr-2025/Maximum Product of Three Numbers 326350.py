# Problem: Maximum Product of Three Numbers - https://leetcode.com/problems/maximum-product-of-three-numbers/description/

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = sorted(nums)
        if_pos = arr[-1] * arr[-2] * arr[-3]
        if_neg = arr[0] * arr[1] * arr[-1]
        ans = max(if_pos, if_neg)
        return ans