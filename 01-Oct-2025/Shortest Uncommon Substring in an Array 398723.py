# Problem: Shortest Uncommon Substring in an Array - https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/description/

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        n = len(arr)
        substring_map = defaultdict(set)

        for i, word in enumerate(arr):
            seen = set()
            for l in range(len(word)):
                for r in range(l+1, len(word)+1):
                    sub = word[l:r]
                    if sub not in seen:
                        substring_map[sub].add(i)
                        seen.add(sub)

        result = []
        for i, word in enumerate(arr):
            candidate = None
            for l in range(1, len(word)+1):
                subs = []
                for start in range(len(word) - l + 1):
                    sub = word[start:start+l]
                    if len(substring_map[sub]) == 1:
                        subs.append(sub)
                if subs:
                    candidate = min(subs)
                    break
            result.append(candidate if candidate else "")
        return result