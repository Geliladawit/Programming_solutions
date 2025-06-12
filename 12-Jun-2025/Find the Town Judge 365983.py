# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        st = set()
        count = [0] * (n + 1)

        for a, b in trust:
            st.add(a)
            count[b] += 1
        for i in range(1, n + 1):
            if i not in st and count[i] == n - 1:
                return i
        
        return -1
