# Problem: Fruit Into Baskets - https://leetcode.com/problems/fruit-into-baskets

class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        n = len(fruits)
        basket = {}
        left = 0
        the_max = 0
        the_sum = 0
        for right, fruit in enumerate(fruits):
            if fruit not in basket:
                basket[fruit] = 0
            basket[fruit] += 1
            the_sum += 1
            while len(basket) > 2:
                left_fruit = fruits[left]
                basket[left_fruit] -= 1
                the_sum -= 1
                if basket[left_fruit] == 0:
                    del basket[left_fruit]
                left += 1
            the_max = max(the_max, the_sum)
        return the_max
