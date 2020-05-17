import sys
from collections import deque
def input():
    return sys.stdin.readline().strip()

tozan = []
gezan = []

def check():
    s = input()
    m = 0
    res = 0
    for i in s:
        if i == "(":
            m += 1 
        else:
            m -= 1
            res = min(res,m)
    if m >= 0:
        tozan.append([res,m])
    else:
        gezan.append([res-m,-m])

N = int(input())
for _ in range(N):
    check()

tozan.sort(reverse=True)
gezan.sort(reverse=True)

t = 0
g = 0

for res,m in tozan:
    if t + res < 0:
        print("No")
        exit()
    t += m

for res,m in gezan:
    if g + res < 0:
        print("No")
        exit()
    g -= m

if t == g:
    print("Yes")
else:
    print("No")
    
    



