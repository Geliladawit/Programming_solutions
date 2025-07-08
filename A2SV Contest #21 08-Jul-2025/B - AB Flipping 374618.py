# Problem: B - AB Flipping - https://codeforces.com/gym/619446/problem/B

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    prefix_A = 0
    prefix_B = 0
    operations = 0
    total_B = 0
    
    for c in s:
        if c == 'B':
            total_B += 1
    for i in range(1,n):
            if s[i - 1] == "A":
                prefix_A += 1
            else:
                prefix_B += 1
            if prefix_A > 0 and total_B - prefix_B > 0:
                operations += 1
    
    print(operations)
