from collections import Counter

S = input()

c = list(Counter(S).values())

o = 0
e = 0

for i in c:
    if i%2 == 0:
        e += i
    else:
        o += 1
        e += i-1

if o == 0:
    print(len(S))
else:
    print(max(1,1+2*((e//2)//o)))


