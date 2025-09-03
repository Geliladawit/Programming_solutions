# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

def insertionSort1(n, arr):
    # Write your code here
    st = arr[-1]
    for i in range(n-2,-1,-1):
        if arr[i] > st:
            arr[i+1] = arr[i]
            print(" ".join(map(str,arr)))
        else:
            arr[i+1] = st
            print(" ".join(map(str,arr)))
            return
    arr[0] = st
    print(" ".join(map(str, arr)))