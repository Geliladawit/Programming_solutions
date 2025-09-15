# Problem: Number of Subarrays With LCM Equal to K - https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            lcm_val = 1
            for j in range(i, n):
                lcm_val = math.lcm(lcm_val, nums[j])
                if lcm_val == k:
                    count += 1
                elif lcm_val > k:
                    break 
        return count