# Problem: Decrypt String from Alphabet to Integer Mapping - https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/description/

class Solution:
    def freqAlphabets(self, s: str) -> str:
        h_map = {str(i): chr(96 + i) for i in range(1, 27)}
        res = []
        i = len(s) - 1
        while i > -1:
            if i >= 2 and s[i] == "#":
                res.append(h_map[s[i-2:i]])
                i -= 3
            else:
                res.append(h_map[s[i]])
                i -= 1
            
        return ''.join(reversed(res))