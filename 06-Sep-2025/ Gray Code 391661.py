# Problem:  Gray Code - https://leetcode.com/problems/gray-code/description/

class Solution:
    def grayCode(self, n: int) -> List[int]:
        def grayCodeSeq(n: int):
            if n == 1:
                return [0, 1]
            prev = grayCodeSeq(n - 1)
            res = prev[:]
            res += [x | (1 << (n - 1)) for x in reversed(prev)]
            return res
        return grayCodeSeq(n)