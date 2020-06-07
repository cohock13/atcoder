from collections import Counter

S = input()
T = input()

s = sorted(list(Counter(S).values()))
t = sorted(list(Counter(T).values()))

if s == t:
    print("Yes")
else:
    print("No")