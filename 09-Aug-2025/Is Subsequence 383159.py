# Problem: Is Subsequence - https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr_s = 0
        ptr_t = 0
        len_s = len(s)
        len_t = len(t)
        
        while ptr_s < len_s and ptr_t < len_t:
            if s[ptr_s] == t[ptr_t]:
                ptr_s += 1
            ptr_t += 1
        
        return ptr_s == len_s