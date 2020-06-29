N,M = map(int,input().split())

C = []
for i in range(N):
    C.append(tuple(map(int,input().split())))

C.sort()

tmp = M
ans = 0
for cost,num in C:
    if tmp - num >= 0:##全部買う
        tmp -= num
        ans += num*cost
    else:
        ans += cost*tmp
        break

print(ans)