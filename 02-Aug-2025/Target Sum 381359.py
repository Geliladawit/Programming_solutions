# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]
        dp[0][0] = 1
        for i in range(len(nums)):
            for cur_sum, count in dp[i].items():
                dp[i + 1][cur_sum + nums[i]] += count
                dp[i + 1][cur_sum - nums[i]] += count
        return dp[len(nums)][target]
