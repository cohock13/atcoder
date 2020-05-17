A,B,M = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = 1e9
for i in range(M):
    x,y,c = map(int,input().split())
    wari = max(a[x-1]+b[y-1]-c,0)
    ans = min(ans,wari)
ans = min(ans,min(a)+min(b))
print(ans)
    
