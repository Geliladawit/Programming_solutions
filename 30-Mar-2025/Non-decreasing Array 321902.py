# Problem: Non-decreasing Array - https://leetcode.com/problems/non-decreasing-array/

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        modified = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if modified:
                    return False
                modified = True
                if i == 0 or nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i + 1]
                else:
                    nums[i + 1] = nums[i]
        return True                
