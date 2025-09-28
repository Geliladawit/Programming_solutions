# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        mp = defaultdict(list)
        for word in dictionary:
            mp[word[0]].append(word)
        for ch in mp:
            mp[ch].sort(key=len)

        st = sentence.split()
        n = len(st)
        for i in range(n):
            if st[i][0] in mp:
                for root in mp[st[i][0]]:
                    if st[i].startswith(root):
                        st[i] = root
                        break

        return " ".join(st)
