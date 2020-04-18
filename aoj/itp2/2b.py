from collections import deque

n,q = map(int,input().split())

S = deque([deque() for _ in range(n)])
for i in range(q):
    query = tuple(map(int,input().split()))

    if query[0] == 0:
        S[query[1]].append(query[2])
    elif query[0] == 1:
        if len(S[query[1]]) != 0:
            print(S[query[1]][0])
    else:
        if len(S[query[1]]) != 0:
            S[query[1]].popleft()