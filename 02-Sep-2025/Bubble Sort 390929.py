# Problem: Bubble Sort - https://www.hackerrank.com/challenges/ctci-bubble-sort/problem


def countSwaps(a):
    # Write your code here
    swaps = 0
    for i in range(n):
        swapped = 0
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j] 
                swapped += 1
        swaps += swapped
        if swapped == 0:
            break
    print(f"Array is sorted in {swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
