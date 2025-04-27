# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        h_map = {}
        for i in s:
            if i not in h_map:
                h_map[i] = 1
            else:
                h_map[i] += 1
        st = []
        for i in s:
            h_map[i] -= 1
            if i in st:
                continue
            while st and st[-1] > i and h_map[st[-1]] > 0 and i not in st:
                st.pop()
            st.append(i)
        return "".join(st)