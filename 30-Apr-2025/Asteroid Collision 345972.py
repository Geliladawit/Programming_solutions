# Problem: Asteroid Collision - https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for i in asteroids:
            while st  and i < 0 < st[-1]:
                if abs(i) == abs(st[-1]):
                    st.pop()
                    break
                elif abs(i) > abs(st[-1]):
                    st.pop()
                else:
                    break
            else:
                if not st or st[-1] < 0 or i > 0:
                    st.append(i)
        return st