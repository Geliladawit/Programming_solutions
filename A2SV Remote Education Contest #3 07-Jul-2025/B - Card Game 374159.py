# Problem: B - Card Game - https://codeforces.com/gym/588094/problem/B

import sys 

input = sys.stdin.readline

def solve():

    n = int(input())

    cards = list(map(int, input().split()))

    cards = [(cards[i], i + 1) for i in range(len(cards))]

    cards.sort(key=lambda x: x[0])

    for i in range(n // 2):

        print(*(cards[i][1], cards[n - i - 1][1]))

if __name__ == '__main__':

    solve()