# Problem: Pascal's Triangle - https://leetcode.com/problems/pascals-triangle/description/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        st = [[1]]
        for i in range(numRows - 1):
            s = [1]
            for j in range(len(st[-1])-1):
                s.append(st[i][j+1] + st[i][j])
            s.append(1)  
            st.append(s)
        return st