# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/description/

class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = []
        for i in s:
            if i != "*":
                st.append(i)
            else:
                st.pop()
                
        return "".join(st)