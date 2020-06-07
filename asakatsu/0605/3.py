N,Q = map(int,input().split())

S = input()

T = S.replace("AC","!?")

csum = [0]*N

s = 0

for i in range(N):
    if T[i] == "?":
        s += 1
    csum[i] = s

for i in range(Q):
    l,r = map(int,input().split())
    print(csum[r-1]-csum[l-1])