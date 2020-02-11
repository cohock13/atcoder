N,M = map(int,input().split())
a = list(map(int,input().split()))

a.sort()

right = M
left = 0

while abs(right-left)>1:
    m = int((right+left)/2)
    if #Kがすべてにおいてある:
        left = m
    else:
        right = m

print(left)


