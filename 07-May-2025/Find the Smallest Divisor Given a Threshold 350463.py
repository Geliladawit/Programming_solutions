# Problem: Find the Smallest Divisor Given a Threshold - https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def div_cal(divisor,s):
            for num in nums:
                s += ceil(num/divisor)
            return s

        low, high = 1, 10**9
        while low <= high:
            divisor = (low + high)//2
            if div_cal(divisor,0) <= threshold:
                high = divisor - 1
            else:
                low = divisor + 1
        return low

            