from collections import Counter

N,M = map(int,input().split())
A = list(map(int,input().split()))

c = Counter(A)

for i,j in zip(c.keys(),c.values()):
    if j > N/2:
        print(i)
        exit()

print("?")

