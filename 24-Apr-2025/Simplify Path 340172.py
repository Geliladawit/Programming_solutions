# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        sp = path.split("/")
        res = []
        for i in sp:
            if i == "..":
                if res:
                    res.pop()
            elif i == "." or i =="":
                continue
            else:
                res.append(i)
        result = "/" + "/".join(res)
        return result
