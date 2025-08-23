# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            twos = twos ^ (ones & num)
            ones = ones ^ num
            mask = ~(ones & twos)
            ones, twos = mask & ones, mask & twos
        return ones
            