def check(X,Y):
    Hs = []
    for x,y,h in xyh:
        if h > 0:
            H = h + abs(x-X) + abs(y-Y)
            Hs.append(H)
        else:
            H = Hs[0]
            if abs(x-X) + abs(y-Y) < H:
                return False
    
    if len(set(Hs)) == 1:
        print(X,Y,Hs[0])
        return True
    else:
        return False

N = int(input())
xyh = [list(map(int,input().split())) for _ in range(N)]
xyh.sort(key=lambda a:a[2],reverse=True)

for i in range(101):
    for j in range(101):
        if check(i,j):
            exit()
