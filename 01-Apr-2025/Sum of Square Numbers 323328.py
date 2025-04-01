# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        # if c == 1:
        #     return True
        # j = c//2
        # i = 0
        # while i <= j:
        #     if (i * i) + (j * j) == c:
        #         return True
        #     elif (i * i) + (j * j) < c:
        #         i += 1
        #     else:
        #         j -= 1
        # return False
        left = 0
        right = int(math.sqrt(c))
        if c == 1 or c == 0:
            return True
        while(left <= right):
            sum = (left * left) + (right * right)
            if sum > c:
                right -= 1
            elif sum < c:
                left += 1
            elif sum == c:
                return True
        return False            