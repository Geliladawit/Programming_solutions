# Problem: Largest Merge of Two Strings - https://leetcode.com/problems/largest-merge-of-two-strings/

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        res = []
        w1 = 0
        n = len(word1)
        m = len(word2)
        w2 = 0
        while w1 < n or w2 < m:
            if word1[w1:] >= word2[w2:]:
                res.append(word1[w1])
                w1 += 1
            else:
                res.append(word2[w2])
                w2 += 1
                
        return ''.join(res)