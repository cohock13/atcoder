X,N = map(int,input().split())
p = list(map(int,input().split()))

ans = 1e10
pos = 0
for i in range(-100,120):
    if i not in p:
        if abs(i-X) < ans:
            pos = i
            ans = abs(i-X)
    
print(pos)