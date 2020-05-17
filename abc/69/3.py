N = int(input())
A = list(map(int,input().split()))

ans = 0

for i in A:
    if i%4 == 0:
        ans += 2
    elif i%2 == 0:
        ans += 1

if ans >= N - int(N%2==1):
    print("Yes")
else:
    print("No")