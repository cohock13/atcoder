from collections import deque

n = int(input())

que = deque()
a = 0
for i in range(n):
    print("-------")
    try:
        order,value = input().split()
        value = int(value)
        if order == "insert":
            que.appendleft(value)
        elif order == "delete":
            try:
                que.remove(value)
                print("removed")
            except:
                a += 1
                print(a)
    except:
        order = input()
        if order == "deleteFirst":
            que.popleft()
            print("poplefted")
        elif order == "deleteLast":
            que.pop()


print(*que)