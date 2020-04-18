from collections import deque

q = int(input())

L = deque()
pointer = 0

for i in range(q):
    query = input().split()

    if query[0] == "0":
        L.appendleft(int(query[1]))
    elif query[0] == "1":
        pointer += int(query[1])
        L.rotate(-int(query[1]))
    else:
        L.popleft()
L.rotate(pointer)
for i in L:
    print(i)