# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        st = ''
        block = False
        for line in source:
            i = 0
            n = len(line)
            while i < n:
                if not block and i < n and line[i:i+2] == "//":
                    break
                elif not block and i < n and line[i:i+2] == "/*":
                    block = True
                    i += 2
                elif block and i < n and line[i:i+2] == "*/":
                    block = False
                    i += 2
                else:
                    if not block:
                        st += line[i]
                    i += 1
            if not block and st:
                res.append(st)
                st = ""
        return res

