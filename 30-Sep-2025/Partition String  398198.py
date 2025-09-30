# Problem: Partition String  - https://leetcode.com/problems/partition-string/description/

class Solution:
    def partitionString(self, s: str) -> List[str]:
        n = len(s)
        seen_seg = set()
        c = ""
        res = []
        for i in range(n):
            c += s[i]
            if c not in seen_seg:
                seen_seg.add(c)
                res.append(c)
                c = ""
        return res