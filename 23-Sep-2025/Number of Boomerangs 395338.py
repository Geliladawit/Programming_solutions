# Problem: Number of Boomerangs - https://leetcode.com/problems/number-of-boomerangs/description/

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for i in points:
            dist_count = {}
            for j in points:
                if i == j:
                    continue
                dx = i[0] - j[0]
                dy = i[1] - j[1]
                d = dx*dx + dy*dy  
                dist_count[d] = dist_count.get(d, 0) + 1
            
            for m in dist_count.values():
                res += m * (m - 1)
        return res