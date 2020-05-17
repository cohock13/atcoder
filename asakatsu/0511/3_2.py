N,L = map(int,input().split())

kuji = []

for _ in range(L):
    kuji.append(list(input()))

pos = list(input())

x,y = L-1,pos.index("o")

while 1:

    if x == -1:
        print(y//2+1)
        break
    try:
        if kuji[x][y+1] == "-":
            y += 2
        else:
            try:
                if kuji[x][y-1] == "-":
                    y -= 2
            except:
                pass
    except:
        try:
            if kuji[x][y-1] == "-":
                y -= 2
        except:
            pass
    
    x -= 1

        