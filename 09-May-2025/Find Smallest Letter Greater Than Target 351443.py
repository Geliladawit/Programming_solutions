# Problem: Find Smallest Letter Greater Than Target - https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, h = 0, len(letters) -1
        if letters[h] <= target[0]:
            return letters[l]
        while l <= h:
            mid = (l+h)//2
            if letters[mid] > target[0]:
                h = mid - 1
            else:
                l = mid + 1
        return letters[l]