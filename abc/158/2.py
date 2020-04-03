N,A,B = map(int,input().split())
ans = 0
tmp = N//(A+B)
ans += tmp*A
N -= (A+B)*tmp
ans += min(A,N)

print(ans)