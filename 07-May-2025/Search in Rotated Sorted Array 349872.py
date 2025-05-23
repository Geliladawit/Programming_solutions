# Problem: Search in Rotated Sorted Array - https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                return mid
            elif target in nums[:mid]:
                high = mid - 1
            else:
                low = mid + 1
