A,V = map(int,input().split())
B,W = map(int,input().split())
T = int(input())

dist = abs(A-B)
if dist == 0:
    print("YES")
    exit()
vel = abs(W-V)

if V*T >= W*T + dist:
    print("YES")
else:
    print("NO")
