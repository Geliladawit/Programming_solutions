# Problem: Subarray Product Less Than K - https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k < 2:
            return 0
        left= 0
        c = 0
        s = 1
        n = len(nums)
        for right in range(n):
            s *= nums[right]
            while s >= k:
                s = s/nums[left]
                left += 1
            c += (right -left + 1)
        return c
        