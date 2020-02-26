import statistics
N = int(input())
A = list(map(int,input().split()))
B = list(A[i]-(i+1) for i in range(N))
B.sort()
b = int(statistics.median(B))
print(sum([abs(A[i-1]-(b+i)) for i in range(1,N+1)]))
