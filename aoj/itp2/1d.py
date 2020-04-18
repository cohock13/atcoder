n,q = map(int,input().split())
L = [[] for _ in range(n)]

for i in range(q):
    query = input().split()

    if query[0] == "0":
        L[int(query[1])].append(query[2])
    elif query[0] == "1":
        print(*L[int(query[1])])
    else:
        L[int(query[1])] = []
