# Problem: Repeated String Match - https://leetcode.com/problems/repeated-string-match/description/

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeat = math.ceil(len(b) / len(a))
        
        if b in a * repeat:
            return repeat
        elif b in a * (repeat + 1):
            return repeat + 1
        else:
            return -1