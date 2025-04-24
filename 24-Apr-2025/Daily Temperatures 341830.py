# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution(object):
    def dailyTemperatures(self, temperatures):
        answer = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
        return answer
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        