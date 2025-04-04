# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_num = 0
        pairs = 0
        ans = []
        nums.sort()
        i = 0
        n = len(nums)
        if n == 1:
            return [0, 1]
        while i < n:
            if i < n - 1 and nums[i] == nums[i + 1]:
                pairs += 1
                i += 2  
            else:
                left_num += 1
                i += 1
        
        ans.append(pairs)
        ans.append(left_num)
        return ans