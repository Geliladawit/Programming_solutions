# Problem: Clear Digits - https://leetcode.com/problems/clear-digits/description/

class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for i in s:
            if i.isdigit():
                if res:
                    res.pop()
            else:
                res.append(i)
        return "".join(res)