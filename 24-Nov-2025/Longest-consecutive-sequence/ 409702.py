# Problem: Longest-consecutive-sequence/ - https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        longest = 0
        for i in num:
            if i - 1 not in num:
                length = 1
                curr = i
                while curr + 1 in num:
                    length += 1
                    curr += 1

                longest = max(length, longest)
        return longest