# Problem: Length of Last Word - https://leetcode.com/problems/length-of-last-word/description/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        st = s.split(" ")
        n = len(st)
        for i in range(n-1,-1,-1):
            if st[i] != "":
                return len(st[i])