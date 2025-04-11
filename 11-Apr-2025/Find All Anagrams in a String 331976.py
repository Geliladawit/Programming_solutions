# Problem: Find All Anagrams in a String - https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        p_count = Counter(p)
        s_count = Counter(s[:len(p) - 1])

        for i in range(len(p) - 1, len(s)):
            curr = s[i]
            s_count[curr] += 1
            if s_count == p_count:
                result.append(i - len(p) + 1)
            s_count[s[i - len(p) + 1]] -= 1
            if s_count[s[i - len(p) + 1]] == 0:
                del s_count[s[i - len(p) + 1]]
        return result
