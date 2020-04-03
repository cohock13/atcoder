N,M = map(int,input().split())
if M == 0:
    if N == 1:
        print(0)
    else:
        print(1)
    exit()
digit = [0]*3

for i in range(M):
    s,c = map(int,input().split())
    s = s-1
    if c == 0:
        c = -1
    if digit[s] == 0:
        digit[s] = c
    elif digit[s] != c:
        print(-1)
        exit()

##print(digit)
if N>=2:
    if digit[0] == -1:
        print(-1)
        exit()
flag = True
for i in range(N):
    if digit[i] != 0:
        flag = False
    if flag:
        digit[i] = 1
        flag = False
    if digit[i] == -1:
        digit[i] = 0
##print(digit)
ans = 0

for i in range(N):
    ans += digit[i]*10**(N-i-1)
if ans == 0:
    ans = 1
print(ans)
        

