# Problem: Find the Number of Distinct Colors Among the Balls - https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        d = {}
        freq = {}
        st = []
        for x, y in queries:
            if x in d:
                old_y = d[x]
                freq[old_y] -= 1
                if freq[old_y] == 0:
                    del freq[old_y]
            d[x] = y
            freq[y] = freq.get(y, 0) + 1
            st.append(len(freq))
        return st