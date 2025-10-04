# Problem: Short Encoding of Words - https://leetcode.com/problems/short-encoding-of-words/

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = set(words)
        def is_suffix(s,words):
            n = len(words)
            for i in words:
                if i != s and i.endswith(s): 
                    return True
            return False
        st = ""
        for s in words:
            if not is_suffix(s,words):
                st += s + "#"
        return len(st)
