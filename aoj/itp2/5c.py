from itertools import permutations

n = int(input())
a = list(map(int,input().split()))

s = []
for i in permutations(sorted(a)):
    s.append(list(i))

for i in range(len(s)):
    if s[i] == a:
        if i > 0:
            print(*s[i-1])
        print(*s[i])
        if i < len(s)-1:
            print(*s[i+1])
        break