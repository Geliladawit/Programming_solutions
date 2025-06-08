# Problem: F - Median Harmony - https://codeforces.com/gym/607756/problem/F

import sys
import threading

def solve():
    import sys, bisect
    input = sys.stdin.readline

    class Fenwick:
        __slots__ = ('n','f')
        def __init__(self, n):
            self.n = n
            self.f = [0] * (n+1)
        def add(self, i, v):
            # i in [1..n]
            f = self.f; n = self.n
            while i <= n:
                f[i] += v
                i += i & -i
        def sum(self, i):
            s = 0; f = self.f
            while i > 0:
                s += f[i]
                i -= i & -i
            return s

    t = int(input())
    out = []
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        # 1) sous‑tableaux de longueur impaire
        odd = ((n+1)//2) * ((n+2)//2)

        # fréquences pour skippper vite les v peu fréquents
        freq = [0]*11
        for x in a:
            freq[x] += 1

        even_good = 0

        # 2) pour chaque valeur v candidate
        for v in range(1, 11):
            if freq[v] < 2:
                continue

            # construire pref_less et pref_eq
            pref_less = [0] * (n+1)
            pref_eq   = [0] * (n+1)
            for i in range(1, n+1):
                ai = a[i-1]
                pref_less[i] = pref_less[i-1] + (1 if ai < v else 0)
                pref_eq[i]   = pref_eq[i-1]   + (1 if ai == v else 0)

            # construire X,Y pour i=0..n
            # A = 2*pref_less, B = 2*(pref_less+pref_eq)
            # X = A - i, Y = B - i
            X = [0] * (n+1)
            Y = [0] * (n+1)
            for i in range(n+1):
                A = 2 * pref_less[i]
                B = 2 * (pref_less[i] + pref_eq[i])
                X[i] = A - i
                Y[i] = B - i

            # on traite par parité
            for parity in (0, 1):
                # collecter points j et queries r
                pts = []   # (xj', yj)
                qs  = []   # (thr_x, thr_y)
                for j in range(0, n):
                    if (j & 1) == parity:
                        pts.append((-X[j], Y[j]))
                for r in range(1, n+1):
                    if (r & 1) == parity:
                        # on veut X[j] >= X[r]+2 et Y[j] <= Y[r]-2
                        # <=> -X[j] <= -X[r]-2  et  Y[j] <= Y[r]-2
                        thr_x = -X[r] - 2
                        thr_y =  Y[r] - 2
                        qs.append((thr_x, thr_y))

                if not pts or not qs:
                    continue

                # tri points et queries par abscisse
                pts.sort(key=lambda p: p[0])
                qs_sorted = sorted(qs, key=lambda q: q[0])

                # coord‑compresser les y des points
                ys_pts = [y for _,y in pts]
                # on n'a pas besoin d'inclure thr_y dans la compression ;
                # on utilisera bisect_right sur ys_pts pour les requêtes.
                ys_sorted = sorted(set(ys_pts))
                fenw = Fenwick(len(ys_sorted))

                ip = 0
                m_pts = len(pts)
                # pour chaque requête par ordre croissant de thr_x
                for thr_x, thr_y in qs_sorted:
                    # on insère tous les pts dont x' <= thr_x
                    while ip < m_pts and pts[ip][0] <= thr_x:
                        yj = pts[ip][1]
                        pos = bisect.bisect_left(ys_sorted, yj) + 1
                        fenw.add(pos, 1)
                        ip += 1
                    # on compte les pts insérés dont yj <= thr_y
                    # => idx = bisect_right(ys_sorted, thr_y)
                    idx = bisect.bisect_right(ys_sorted, thr_y)
                    if idx:
                        even_good += fenw.sum(idx)

        out.append(str(odd + even_good))

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    # pour désactiver le recouvrement d'I/O en CPython
    threading.Thread(target=solve).start()