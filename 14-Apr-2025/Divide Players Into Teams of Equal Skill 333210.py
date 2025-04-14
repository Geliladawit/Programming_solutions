# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        s = 0
        i = 0
        j = len(skill) - 1
        n = skill[i] + skill[j]
        while i < j:
            if n == skill[i+1] + skill[j-1]:
                s = s + (skill[i] * skill[j])
                i += 1
                j -= 1
            else:
                return -1
        return s