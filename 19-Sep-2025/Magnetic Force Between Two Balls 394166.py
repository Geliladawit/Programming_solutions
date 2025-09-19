# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        low, high = 1, position[-1] - position[0]
        
        def solve(dist):
            count = 1
            last_position = position[0]
            
            for i in range(1, len(position)):
                if position[i] - last_position >= dist:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        return True
            return False
        
        best_dist = 0
        while low <= high:
            mid = (low + high) // 2
            if solve(mid):
                best_dist = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return best_dist