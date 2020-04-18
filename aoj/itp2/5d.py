from itertools import permutations

a = [i+1 for i in range(int(input()))]

for i in permutations(a):
    print(*i)
