X,Y = map(int,input().split())

for k in range(X+1):
    t = X-k 
    if 2*k + 4*t == Y:
        print("Yes")
        exit()
print("No")