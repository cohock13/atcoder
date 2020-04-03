N = int(input())
blue = {}
for i in range(N):
    tmp = input()
    if tmp in blue:
        blue[tmp] += 1
    else:
        blue[tmp] = 1
M = int(input())
red = {}
for i in range(M):
    tmp = input()
    if tmp in red:
        red[tmp] += 1
    else:
        red[tmp] = 1

keys_r = list(blue.keys())
values_r = list(blue.values())
A = []
for i in range(len(keys_r)):
    A.append([keys_r[i],values_r[i]])

ans = 0
for i in range(len(A)):
    tmp = A[i][1]
    if A[i][0] in red:
        tmp -= 1
    ans = max(ans,tmp) 

print(ans)