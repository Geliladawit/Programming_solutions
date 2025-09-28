# Problem: Search Suggestions System - https://leetcode.com/problems/search-suggestions-system/

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        prod = sorted(products)
        res = []
        for i in range(len(searchWord)):
            st = []
            for j in range(len(products)):
                if len(st) == 3:
                    break
                if ord(searchWord[0]) < ord(prod[j][0]):
                    break
                if prod[j][:i+1] == searchWord[:i+1]:
                    st.append(prod[j])
            res.append(st)
        print(prod)
        return res