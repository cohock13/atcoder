from collections import deque

q = int(input())

que = deque()
for i in range(q):
    query = input().split()

    if query[0] == "0":
        que.append(query[1])
    elif query[0] == "1":
        print(que[int(query[1])])
    else:##popBack
        que.pop()


