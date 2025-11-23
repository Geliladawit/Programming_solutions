# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        h_map = defaultdict(int)
        n = len(heights)
        for i in range(n):
            h_map[heights[i]] = names[i]
        heights.sort(reverse = True)
        for i in range(n):
            names[i] = h_map[heights[i]]

        return names
