# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        longest = ""
        c = 0
        for left in range(n):
            for right in range(n-1,-1,-1):
                sub1 = s[left:right+1]
                if sub1 == sub1[::-1]:
                    if c < len(sub1):
                        c = len(sub1)
                        longest = sub1
                    break
        return longest

