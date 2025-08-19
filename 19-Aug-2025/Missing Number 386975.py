# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for x in nums:
            res ^= x
        for i in range(n+1):
            res ^= i
        return res
            