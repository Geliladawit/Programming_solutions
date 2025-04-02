# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution(object):
    def subarraysDivByK(self, nums, k):
        t_sum = 0
        ans = 0
        count = defaultdict(int)
        count[0] = 1
        for i in nums:
            t_sum  += i
            re = t_sum % k

            if re in count:
                ans += count[re]
            count[re] += 1
        return ans