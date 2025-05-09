# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canCarry(capacity,days):
            runningSum = 0
            for i in range(len(weights)):
                runningSum += weights[i]
                if runningSum > capacity:
                    days -= 1 
                    runningSum = weights[i] 
            return days >= 1                
        low,high = max(weights) - 1, sum(weights) + 1
        while high > low + 1:
            mid = low + (high - low) // 2
            if canCarry(mid,days):
                high = mid
            else:
                low = mid
        return high