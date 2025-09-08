# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/description/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
            
        def radix_sort(arr: List[int]) -> List[int]:
            max_num = max(arr)
            exp = 1
            while max_num // exp > 0:
                count = [0] * 10
                output = [0] * len(arr)
                for num in arr:
                    index = (num // exp) % 10
                    count[index] += 1
                for i in range(1, 10):
                    count[i] += count[i - 1]
                for num in reversed(arr):
                    index = (num // exp) % 10
                    output[count[index] - 1] = num
                    count[index] -= 1
                arr = output
                exp *= 10
            return arr

        nums = radix_sort(nums)
        l, r,m = 0, n - 1,-1
        while l < r:
            m = max(m, nums[l+1] - nums[l], nums[r] -  nums[r-1])
            l += 1
            r -= 1
        return m