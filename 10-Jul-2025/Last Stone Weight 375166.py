# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg = [-s for s in stones]
        heapify(neg)

        while len(neg) > 1:
            stone_one = -heappop(neg)
            stone_two = -heappop(neg)
            if stone_one != stone_two:
                heappush(neg, -(stone_one - stone_two))
        return -neg[0] if neg else 0