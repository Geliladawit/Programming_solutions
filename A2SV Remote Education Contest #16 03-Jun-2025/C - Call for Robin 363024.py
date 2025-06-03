# Problem: C - Call for Robin - https://codeforces.com/gym/613405/problem/C

t = int(input())
for _ in range(t):
    size = int(input())
    nums = list(map(int, input().split()))
 
    if size < 3:
        print(-1)
        continue
 
    nums.sort()
    sumNums = sum(nums)
    minNum = max(0, (2*size * nums[size // 2] - sumNums + 1))
 
    print(minNum)