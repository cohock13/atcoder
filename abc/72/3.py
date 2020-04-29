N = int(input())
A = list(map(int,input().split()))

num = [0]*(max(A)+2)

for i in A:
    num[i] += 1
m = max(A)
ans = 0
for i in range(0,max(A)+2):
    if i == 0:
        tmp = num[i] + num[i+1]
    elif i == m+1:
        tmp = num[i-1] + num[i]
    else:
        tmp = num[i-1] + num[i] + num[i+1]
    ans = max(ans,tmp)

print(ans)