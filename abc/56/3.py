from itertools import accumulate

X = int(input())

csum = accumulate([i+1 for i in range(100000)])

for i,s in enumerate(csum):
    if s >= X:
        print(i+1)
        break

    
