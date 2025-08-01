# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        memo = [[-1]*len(text2) for i in range(len(text1))]
        def dp(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
                        
            if memo[i][j] == -1:
                
                if text1[i] == text2[j]:
                    memo[i][j] = 1 + dp(i+1, j+1)     
                else:
                    memo[i][j] = max(dp(i+1, j), dp(i, j+1))
            return memo[i][j]      
        return dp(0, 0)
