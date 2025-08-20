# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        x = bin(num)[2:]
        complement = ""
        for i in x:
            if i == "1":
                complement += "0"
            else:
                complement += "1"
        ans = int(complement, 2)
        print(complement)
        return ans