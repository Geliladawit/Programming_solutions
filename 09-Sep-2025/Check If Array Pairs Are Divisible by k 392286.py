# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        no_pairs = 0
        counter = Counter()
        for i in range(len(arr)):
            if counter[arr[i] % k]:  
                no_pairs += 1
                counter[arr[i] % k] -= 1
            else:
                counter[-arr[i] % k] += 1 
        
        return no_pairs == len(arr) // 2
