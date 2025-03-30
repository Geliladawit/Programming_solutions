# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        st = ""
        
        for i in range(len(strs[0])):
            for j in range(1,len(strs)) :
                if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                    return st
            st += strs[0][i]
        return st 