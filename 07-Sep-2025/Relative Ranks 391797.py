# Problem: Relative Ranks - https://leetcode.com/problems/relative-ranks/description/

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        answer = [""] * n
        temp = score[:]   
        place = 1
        for _ in range(n):
            m = max(temp)
            idx = score.index(m)   
            if place == 1:
                answer[idx] = "Gold Medal"
            elif place == 2:
                answer[idx] = "Silver Medal"
            elif place == 3:
                answer[idx] = "Bronze Medal"
            else:
                answer[idx] = str(place)
            place += 1
            temp.remove(m) 
        return answer
