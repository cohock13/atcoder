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
        gezan.append([res-m,res,m])

N = int(input())
for _ in range(N):
    check()

tozan.sort(reverse=True)
gezan.sort()
##print(tozan,gezan)
b = 0

for res,m in tozan:
    if b + res < 0:
        print("No")
        exit()
    b += m

for _,res,m in gezan:
    if b + res < 0:
        print("No")
        exit()
    b += m

if b == 0:
    print("Yes")
else:
    print("No")
    
    