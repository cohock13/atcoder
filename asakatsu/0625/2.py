N,M = map(int,input().split())
solved = [0]*(N+1)
penalty = [0]*(N+1)

ac = 0
wa = 0
for _ in range(M):
    a,b = input().split()
    a = int(a)

    if not solved[a]:
        if b == "AC":
            wa += penalty[a]
            solved[a] = 1
        else:
            penalty[a] += 1

print(sum(solved),wa)