# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        # i = 0
        # j = len(people) - 1
        # s = 0
        # people.sort()
        # while i <= j:
        #     if i == j:
        #         s += 1 
        #         i += 1
        #     elif people[j] + people[i] <= limit:
        #         s += 1
        #         i += 1
        #         j -= 1
        #     else:
        #         s += 1
        #         j -= 1
        # return s
    def numRescueBoats(self, people, limit):
        people.sort()
        left = 0
        right = len(people) - 1
        count = 0
        while(left <= right):
            if people[left] + people[right] > limit:
                count += 1
                right -= 1
            elif people[left] + people[right] <= limit:
                count += 1
                right -= 1
                left += 1
            else:
                count += 1
        return count
