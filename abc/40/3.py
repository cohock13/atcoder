N = int(input())
a = list(map(int,input().split()))

cost = [0]*N
cost[1] = abs(a[1]-a[0])

for i in range(2,N):
    cost[i] = min(cost[i-1]+abs(a[i]-a[i-1]),cost[i-2]+abs(a[i]-a[i-2]))

print(cost[-1])