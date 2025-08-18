# Problem: A - Maxim vs. Yogurt: The Great Discount Battle - https://codeforces.com/gym/629689/problem/A

t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    amount = min(n * a, (n %2)* a + n//2 * b )
    print(amount)