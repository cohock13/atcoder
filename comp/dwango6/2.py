def solve():
    N = int(input())
    x = list(map(int,input().split()))
    
    mod = int(1e9+7)
    inv = [0] * N
    for i in range(1, N):
        inv[i] = pow(i, mod - 2, mod)
    for i in range(2, N):
        inv[i] = (inv[i] + inv[i - 1]) % mod
    print(*inv)
    distance = []
    for i in range(N-1):
        distance.append((x[i+1]-x[i]))
        
    inv_sum = [0]*N
    inv_sum[0] = 1
    for i in range(1,N):
        inv_sum[i] = (inv_sum[i-1]+1/(i+1))
    
    factorial = 1
    for i in range(1,N):
        factorial *= (i%mod)

    ans = 0
    for i in range(N-1):
        tmp = (factorial*inv_sum[i])%mod
        ans += (distance[i]*tmp)
    
    print(int(ans%mod))

if __name__ == "__main__":
    solve()


