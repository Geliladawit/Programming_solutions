# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        target = sum(nums) - x
        left = 0
        max_sub = -1
        running_sum = 0
        for right in range(len(nums)):
            running_sum += nums[right]
            while running_sum > target and left <= right:
                running_sum -= nums[left]
                left += 1
            if target == running_sum:
                max_sub = max(max_sub, right - left + 1)
        return -1 if max_sub == -1 else len(nums) - max_sub
        