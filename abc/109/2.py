N = int(input())
W = []
flag = 0
for i in range(N):
    tmp = input()
    if tmp in W:
        flag = 1
    W.append(tmp)

if flag:
    print("No")
    exit()
    
ans = "Yes"

for i in range(N):
    tmp = W[i]
    if i != 0:
        if tmp[0] != l:
            ans = "No"
            break
    l = tmp[-1]

print(ans)
        