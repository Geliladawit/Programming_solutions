# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        x = sorted(c.items(), key=lambda item: (-item[1], item[0]))
        st = []
        for w,count in x[:k]:
            st.append(w)
        return st