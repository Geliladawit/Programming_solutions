# Problem: K Radius Subarray Averages - https://leetcode.com/problems/k-radius-subarray-averages/description/

class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        result = [-1] * n
        if n < k *2 +1:
            return result
        subarray_sum = sum(nums[:2*k+1])
        result[k] = subarray_sum// (2*k+1)
        for i in range(k+1,n-k):
            subarray_sum += (nums[i+k] -  nums[i-k-1])
            result[i] = subarray_sum// (2*k+1)
        return result
