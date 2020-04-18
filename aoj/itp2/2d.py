from collections import deque
import sys
sys.setrecursionlimit(10**9)
def input():
    return sys.stdin.readline().strip()
n,q = map(int,input().split())

L = deque(deque() for i in range(n))

for i in range(q):
    query = input().split()

    if query[0] == "0":
        L[int(query[1])].append(query[2])
    elif query[0] == "1":
        print(" ".join(L[int(query[1])]))
    else:
        s = int(query[1])
        t = int(query[2])
        if len(L[s]):
            if len(L[t]) == 0:
                L[t] = L[s]
            elif len(L[t]) == 1:
                L[s].appendleft(L[t][0])
                L[t] = L[s]
            else:
                L[t].extend(L[s])
        elif len(L[s]) == 1:
            L[t].append(L[t][0])
        L[s] = deque()