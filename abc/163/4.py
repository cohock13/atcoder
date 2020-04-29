N,K = map(int,input().split())

mod = int(1e9+7)

##O(K)
upper = 0
for i in reversed(range(N+1-K,N+1)):
    upper += i
upper_point = N-K
##O(K)
lower = 0
for i in range(K):
    lower += i
lower_point = K
ans = 0

for i in range(K,N+2):
    ##print("N:",i,upper-lower+1)
    
    ans += upper - lower + 1
    upper += upper_point
    lower += lower_point

    upper_point -= 1
    lower_point += 1

print(ans%mod)
