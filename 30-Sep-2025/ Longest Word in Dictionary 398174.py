# Problem:  Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/description/

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        words.sort(key=len)
        valid = {""}
        answer = ""
        for w in words:
            if w[:-1] in valid:
                valid.add(w)
                if len(w) > len(answer) or (len(w) == len(answer) and w < answer):
                    answer = w
        return answer