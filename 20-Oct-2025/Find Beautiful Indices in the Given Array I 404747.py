# Problem: Find Beautiful Indices in the Given Array I - https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/description/

import collections

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        n_s = len(s)
        n_a = len(a)
        n_b = len(b)

        def find_all_occurrences(text, pattern):
            indices = []
            start = 0
            while True:
                idx = text.find(pattern, start)
                if idx == -1:
                    break
                indices.append(idx)
                start = idx + 1
            return indices

        a_idx = find_all_occurrences(s, a)
        b_idx = find_all_occurrences(s, b)
        res = []
        ptr_b = 0   
        for i_a in a_idx:
            while ptr_b < len(b_idx) and b_idx[ptr_b] < i_a - k:
                ptr_b += 1
            if ptr_b < len(b_idx) and b_idx[ptr_b] <= i_a + k:
                res.append(i_a)
        
        return res