n,m=map(int,input().split())
s=[list(map(int,input().split())) for i in range(m)]
p=list(map(int,input().split()))
ans=0
for i in range(2**n):
    for j in range(m):
        t=0
        for k in s[j][1:]:
            if(((i>>(k-1)))&1==1):
                t+=1
        if(t%2!=p[j]):
            break
    else:
        ans+=1
print(ans)