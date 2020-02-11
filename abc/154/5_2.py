def main():
    N = list(map(int, input()))
    K = int(input())
    k = len(N)
    mod = 1000000007
    # 桁数 dp[mod D]
    # dp = [0] * D
    # temp = 0
    for i in range(k):
        un = N[i]
        dp_n = [0] * K
        for j, d in enumerate(dp):
            for l in range(0, un):
                 dp_n[(j+l) % D] += d + (j == temp)
            for l in range(un, 10):
                dp_n[(j+l) % D] += d
        dp = [d % mod for d in dp_n]
        temp = (temp + un) % D
    print((dp[0] - 1) % mod)
 
main()