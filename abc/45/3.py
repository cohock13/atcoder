##2^(|S|-1)
from copy import deepcopy
from collections import deque

S = input()

s = deque([])
for i in S:
    s += [i]
    s += [""]
s.pop()

ans = 0
l = len(S)

for n in range(2**(l-1)):
    tmp = deepcopy(s)
    for i in range(l-1):
        if (n>>i)&1:
            tmp[2*i+1] = "+"
    ans += eval("".join(tmp))

print(ans)