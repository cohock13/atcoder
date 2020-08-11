A,B,C = map(int,input().split())
K = int(input())

cnt = 0
for i in range(100):
    if A >= B:
        B *= 2
        cnt += 1

for i in range(100):
    if B >= C:
        C *= 2
        cnt += 1

if cnt > K:
    print("No")
else:
    print("Yes")