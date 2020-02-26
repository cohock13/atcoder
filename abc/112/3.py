N = int(input())

xyh = []
not_zero = -100
flag_zero = True

for i in range(N):
    x,y,h = map(int,input().split())
    if h > 0 and flag_zero:
        not_zero = i
        flag_zero = False
    xyh.append([x,y,h])

for i in range(101):
    for j in range(101):

        Cx = i
        Cy = j
        H = xyh[not_zero][2] + abs(Cx-xyh[not_zero][0]) + abs(Cy-xyh[not_zero][1])
        ans = True

        for x,y,h in xyh:
            tmp_h = h+abs(Cx-x)+abs(Cy-y)
            if h>0:
                if tmp_h != H:
                    ans = False
                    break
           else:
                if H - abs(Cx-x) -abs(Cy-y) > 0:
                    ans = False
                    break
            
        if ans:
            print(Cx,Cy,H)
            exit() 
            


            

