from collections import deque

que = deque()
q = int(input())

for i in range(q):
    query = input().split()

    if query[0] == "0":
        if query[1] == "0":
            que.appendleft(query[2])
        else:
            que.append(query[2])
    elif query[0] == "1":
        print(que[int(query[1])])
    else:
        if query[1] == "0":
            que.popleft()
        else:
            que.pop()
