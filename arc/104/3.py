N = int(input())

ab = list(list(map(int,input().split())) for _ in range(N))

##入力データの時点で間違っているかどうか
def check():
    ##「同じ階において出入りは0人」
    tmp = []
    negative = 0
    for a,b in ab:
        if a == -1:
            negative += 1
        else:
            tmp.append(a)
        if b == -1:
            negative += 1
        else:
            tmp.append(b)
    
    if len(set(tmp)) + negative != 2*N:
        return False
    
    ##「同じ階にいるときにおいてC_i == C_j」

    tmp = []

    for a,b in ab:

        if a > 0 and b > 0:
            tmp.append([a,b,b-a-1])

    for i in range(len(tmp)):
        for j in range(len(tmp)):
            if same_time_not_same_c(i,j,tmp):
                return False
        
    return True

def same_time_not_same_c(i,j,tmp):
    return not(tmp[i][1] < tmp[j][0] or tmp[j][1] < tmp[i][0]) and (tmp[j][2] != 1 or tmp[i][2] != 1)
                

print("Yes" if check() else "No")


