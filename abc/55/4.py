def simulate(p):

    que = [""]*N
    que[0] = p[0]
    que[1] = p[1]

    for i in range(1,N-1):
        if s[i] == "o":
            if que[i] == "S" and que[i-1] == "S":
                que[i+1] = "S"
            elif que[i] == "S" and que[i-1] == "W":
                que[i+1] = "W"
            elif que[i] == "W" and que[i-1] == "S":
                que[i+1] = "W"
            else:
                que[i+1] = "S"
        else:
            if que[i] == "S" and que[i-1] == "S":
                que[i+1] = "W"
            elif que[i] == "S" and que[i-1] == "W":
                que[i+1] = "S"
            elif que[i] == "W" and que[i-1] == "S":
                que[i+1] = "S"
            else:
                que[i+1] = "W"

    if check(que):
        tmp = ""
        for p in que:
            p += tmp
        print(p)
        exit()

def check(que):
    flag = True
    for i in range(N):
        if not flag:
            return False

        if i == 0:
            if
        elif i == N-1:
        
        else:
    
    return True
                
N = int(input())
s = tuple(input().split())



