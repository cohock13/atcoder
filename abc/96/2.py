N = list(map(int,input().split()))
K = int(input())
N.sort()
for i in reversed(range(K)):
    N[-1] *= 2
    N.sort()

print(sum(N))