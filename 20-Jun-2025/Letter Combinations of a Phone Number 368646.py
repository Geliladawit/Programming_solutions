# Problem: Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_map = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        st = []

        def backtracker(i, s):
            if len(s) == len(digits):
                st.append(s)
                return
            for j in letter_map[digits[i]]:
                backtracker(i + 1, s + j)
        if digits:
            backtracker(0, "")
        return st