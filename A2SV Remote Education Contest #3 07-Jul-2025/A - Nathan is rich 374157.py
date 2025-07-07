# Problem: A - Nathan is rich - https://codeforces.com/gym/588094/problem/A

for _ in range(int(input())):
    n = int(input())
    cars = n//4
    n-=cars*4
    bikes = n//2
    print(cars + bikes)