from collections import deque

def solve(N,A,B,C,D):

    que = deque()
    res = 1e30
    que.append((1,D))

    while que:

        n,cost = que.popleft()

        if n == N:
            res = min(res,cost)
            continue
        elif n > N:
            res = min(res,cost+D*abs(N-n))
            continue
        else:
            que.append((n*2,cost+A))
            que.append((n*3,cost+B))
            que.append((n*5,cost+C))
            que.append((n+1,cost+D))

    print(res)
    return

N,A,B,C,D = map(int,input().split())
solve(N,A,B,C,D)
