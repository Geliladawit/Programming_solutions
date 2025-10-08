# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

def prime_factors(num):
    prime_factors_set = set()
    d = 2
    while d * d <= num:
        while num % d == 0:
            prime_factors_set.add(d)
            num //= d
        d += 1
    if num > 1:
        prime_factors_set.add(num)
    return prime_factors_set
n = int(input())
cnt_almost_prime = 0
for i in range(n + 1):
    prime_factors_set = prime_factors(i)
    if len(prime_factors_set) == 2:
        cnt_almost_prime += 1

print(cnt_almost_prime)