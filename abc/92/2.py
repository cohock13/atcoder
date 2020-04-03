N = int(input())
D,X = map(int,input().split())
ans = 0
for i in range(N):
    A = int(input())
    tmp = 1
    while tmp <= D:
       ans += 1
       tmp += A

print(ans+X) 