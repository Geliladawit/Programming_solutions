# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        mask, output = 0, 0
        for i in range(31, -1, -1):
            mask |= (1 << i)
            found = set([n & mask for n in nums])
            temp = output | (1 << i)
            for f in found:
                if (f ^ temp) in found:
                    output = temp
                    break
        return output