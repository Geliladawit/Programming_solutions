# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        res = 0
        for i in range(n):
            for j in range(i+1,n):
                s1 = set(words[i])
                s2 = set(words[j])
                if s1.isdisjoint(s2):
                    res = max(res, len(words[i]) * len(words[j]) ) 
        return res