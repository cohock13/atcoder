S = input()[::-1]
P = [0]*(len(S)+1)
a = 0
for i,j in enumerate((S)):
    a = (a+int(j)*pow(10,i,2019))%2019
    P[i] = a

dp = [0]*2019
for i in P:
    dp[i%2019] += 1
print(sum([i*(i-1)//2 for i in dp]))
