from itertools import product

S = input()
N = int(input())
s = []
for i in product(S,repeat=2):
    s.append("".join(i))

print(s[N-1])