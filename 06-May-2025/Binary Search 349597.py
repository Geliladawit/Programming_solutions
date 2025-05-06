# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if target not in nums:
        #     return -1
        # low, high = 0, len(nums) -1
        # while low<=high:
        #     mid = (high + low)//2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] > target:
        #         high = mid - 1
        #     else:
        #         low = mid + 1

        if target not in nums:
            return -1
        else:
            idx = nums.index(target)
            return idx