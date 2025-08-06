# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        st = [[1]]
        for i in range(rowIndex):
            s = [1]
            for j in range(len(st[-1])-1):
                s.append(st[i][j+1] + st[i][j])
            s.append(1)  
            st.append(s)
        return st[-1]