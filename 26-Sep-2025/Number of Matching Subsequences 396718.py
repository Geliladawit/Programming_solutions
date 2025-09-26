# Problem: Number of Matching Subsequences - https://leetcode.com/problems/number-of-matching-subsequences/

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = defaultdict(list)
        for w in words:
            waiting[w[0]].append(iter(w[1:]))
        count = 0
        for ch in s:
            old = waiting[ch]
            waiting[ch] = []
            for it in old:
                nxt = next(it, None)
                if nxt:
                    waiting[nxt].append(it)
                else:
                    count += 1
        return count