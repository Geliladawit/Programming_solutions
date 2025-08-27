# Problem: Decode XORed Permutation - https://leetcode.com/problems/decode-xored-permutation/description/?envType=problem-list-v2&envId=bit-manipulation

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        xor1 = 0
        for i in range(1, n+1):
            xor1 ^= i

        xor2 = 0
        for i in range(1, n-1, 2):
            xor2 ^= encoded[i]

        ans = []
        ans.append(xor1 ^ xor2)
        for i in range(n-1):
            ans.append(encoded[i] ^ ans[-1])

        return ans
