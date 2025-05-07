# Problem: Find Peak Element - https://leetcode.com/problems/find-peak-element

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        num = max(nums)
        idx = nums.index(num)
        return idx
            