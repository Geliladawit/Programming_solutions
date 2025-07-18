# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbits = Counter(answers)
        print(rabbits)
        count = 0
        for i in rabbits:
            if i == 0:
                count += rabbits[i]
            else:
                count += (i + 1) * ((rabbits[i] + i) // (i + 1))
        return count