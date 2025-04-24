# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution(object):
    def isValid(self, s):
        stack = []
        all_Mapped = { "}" : "{", "]" : "[", ")" : "("}
        for one_parentheses in s:
            if one_parentheses in all_Mapped:
                if stack and stack[-1] == all_Mapped[one_parentheses]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(one_parentheses)
        return True if not stack else False  
        """
        :type s: str
        :rtype: bool
        """
        