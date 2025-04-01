# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution(object):
    def productExceptSelf(self, nums):
        answer = [1] * len(nums)
        before = 1
        i = 0
        while i < len(nums):
            answer[i] *= before
            before *= nums[i]
            i += 1
        after = 1
        i = len(nums) - 1
        while i >= 0:
            answer[i] *= after
            after *= nums[i]
            i -= 1
        return answer
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        