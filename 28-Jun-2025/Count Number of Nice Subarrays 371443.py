# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def most(k):
            count = 0
            left = 0
            odd_count = 0
            
            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    odd_count += 1
                
                while odd_count > k:
                    if nums[left] % 2 == 1:
                        odd_count -= 1
                    left += 1
                
                count += right - left + 1
            
            return count
        return most(k) - most(k - 1)