# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        maxx = float("-inf")
        for right in range(len(s)):
            count[s[right]] += 1
            size = right - left + 1
            most = max(count.values())
            if size - most > k:
                count[s[left]] -= 1
                left += 1
            else:
                maxx = max(size, maxx)
        return maxx

