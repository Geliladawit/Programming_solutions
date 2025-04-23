# Problem: First Unique Character in a String - https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=problem-list-v2&envId=queue

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        h_map = OrderedDict()
        for i in s:
            if i not in h_map:
                h_map[i] = 1
            else:
                h_map[i] += 1
        res = -1
        for i in h_map:
            if h_map[i] == 1:
                res = s.index(i)
                break
        return res