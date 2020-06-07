N = int(input())
A = list(map(int,input().split()))

if N <= 2:
    print(1)
    exit()

d = []
for i in range(N-1):
    if A[i+1] - A[i] > 0:
        d.append(1)
    elif A[i+1] - A[i] < 0:
        d.append(-1)

flag = [True]*len(d)

ans = 1
for i in range(len(d)-1):
    if flag[i]:
        if d[i] == -d[i+1]:
            ans += 1
            flag[i+1] = False
print(ans)
