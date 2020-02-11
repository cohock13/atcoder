N = int(input())
l = list(map(int,input().split()))
 
S = sum(l)
 
M = max(l)
 
if S - M > M:
    print("Yes")
else:
    print("No")