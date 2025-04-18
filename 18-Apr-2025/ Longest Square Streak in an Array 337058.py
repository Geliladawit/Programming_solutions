# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

class Solution(object):
    def longestSquareStreak(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(set(nums))
        n = len(nums)
        the_max = max(nums) if nums else 0
        longest_streak = 0
        num_s = set(nums)
        for i in range(n):
            j = nums[i]
            current_streak = 0
            while j <= the_max:
                if j in num_s:
                    current_streak += 1
                    j = j * j  
                else:
                    break
            longest_streak = max(longest_streak, current_streak)
        return longest_streak if longest_streak > 1 else -1 
