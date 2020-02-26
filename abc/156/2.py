import math

N,K = map(int,input().split())

ans = math.log(N)//math.log(K)

print(int(ans+1))