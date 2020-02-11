tmp = input()
digit = len(tmp)
N = int(tmp)

dp = [[0]*digit]*10


for i in range(digit):
    for j in range(10):


print(sum(dp[digit]))