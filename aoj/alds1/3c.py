from collections import deque

n = int(input())

que = deque()

for i in range(n):
    order = input()

    if order == "deleteFirst":
        que.popleft()
    elif order == "deleteLast":
        que.pop()

    else:
        order,value = order.split()
        value = int(value)
        if order == "insert":
            que.appendleft(value)
        elif order == "delete":
            try:
                que.remove(value)
            except:
                pass

print(*que)