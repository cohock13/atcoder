A,B,C,D = map(int,input().split())

time = [0]*101

for i in range(A,B):
    time[i] += 1
for i in range(C,D):
    time[i] += 1

ans = 0
for i in time:
    if i == 2:
        ans += 1

print(ans)