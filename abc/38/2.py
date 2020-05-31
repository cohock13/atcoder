H,W = map(int,input().split())
S,T = map(int,input().split())

if H == S or H == T or W == S or W == T:
    print("YES")
else:
    print("NO")