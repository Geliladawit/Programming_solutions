# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix)-1
        while low <= high:
            mid = (low + high)//2
            if target in matrix[mid]:
                return True
            elif matrix[mid][-1] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False