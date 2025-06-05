# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtracker(i, current, total):
            if total == target:
                res.append(current.copy())
                return
            if i >= len(candidates) or total > target:
                return

            current.append(candidates[i])
            backtracker(i, current, total + candidates[i])
            current.pop()
            backtracker(i + 1, current, total)

        backtracker(0, [], 0)
        return res