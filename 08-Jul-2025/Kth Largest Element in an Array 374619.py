# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        neg_nums = [-x for x in nums]
        heapify(neg_nums)

        for _ in range(k - 1):
            heappop(neg_nums)

        return -heappop(neg_nums)