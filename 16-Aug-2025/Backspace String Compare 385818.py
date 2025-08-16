# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution(object):
    def backspaceCompare(self, s, t):
        def backspaceHandler(s):
            st = []
            for i in s:
                if i != "#":
                    st.append(i)
                elif st:
                    st.pop()
            return "".join(st)
        return backspaceHandler(s) == backspaceHandler(t)
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        