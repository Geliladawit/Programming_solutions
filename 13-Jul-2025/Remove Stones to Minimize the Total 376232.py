# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        mx = [-pile for pile in piles]
        heapify(mx)
        for _ in range(k):
            max_num = -heappop(mx)
            heappush(mx, -ceil(max_num / 2))

        return -sum(mx)