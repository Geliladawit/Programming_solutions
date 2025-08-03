# Problem: Edit Distance - https://leetcode.com/problems/edit-distance/description/

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        memo = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1) ]
        for i in range(len(word2) + 1):
            memo[len(word1)][i] = len(word2) - i
        for i in range(len(word1) + 1):
            memo[i][len(word2)] = len(word1) - i

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    memo[i][j] = memo[i+1][j+1]
                else:
                    memo[i][j] = 1 + min(memo[i+1][j], memo[i][j+1], memo[i+1][j+1])
        return memo[0][0]