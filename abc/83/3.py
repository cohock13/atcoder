X,Y = map(int,input().split())

ans = [X]
while 1:
    X *= 2
    if X <= Y:
        ans.append(X)
    else:
        break
print(len(ans))
    
