# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = list()
        curr = 0
        for i in s:
            if i == "(":
                st.append(curr)
                curr = 0
            else:
                curr = st.pop() + max(curr * 2, 1)
        return curr