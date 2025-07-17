# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        def move(t, md, count):
            if t == 1:
                return count
            if t % 2 != 0:
                return move(t - 1, md, count + 1)
            elif t % 2 == 0 and md > 0:
                return move(t // 2, md - 1, count + 1)
            elif t % 2 == 0 and md == 0:
                return count + t - 1
        return move(target, maxDoubles, 0)