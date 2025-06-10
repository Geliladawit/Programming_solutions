# Problem: E - Final Boss - https://codeforces.com/gym/609279/problem/E

import sys
import threading

def solve():
    input_data = sys.stdin.read().split()
    it = iter(input_data)
    T = int(next(it))
    out_lines = []

    for _ in range(T):
        n = int(next(it))
        x = int(next(it))
        src = [0] * n
        P = 0

        for i in range(n):
            val = int(next(it))
            src[i] = val
            if val == x:
                P = i

        l = 0
        r = n
        while r - l > 1:
            m = (l + r) // 2
            if src[m] <= x:
                l = m
            else:
                r = m

        out_lines.append("1")
        out_lines.append(f"{P+1} {l+1}")

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    threading.Thread(target=solve).start()