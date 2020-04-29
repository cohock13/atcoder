N = int(input())
A = list(map(int,input().split()))

p = [0]*N

for i in A:
    p[i-1] += 1

for i in p:
    print(i)