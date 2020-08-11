from collections import Counter

N,M = map(int,input().split())
A = list(map(int,input().split()))
c = Counter(A)
for i,n in zip(c.keys(),c.values()):
    if n > N/2:
        print(i)
        exit()
print("?")
    
