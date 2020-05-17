from collections import Counter

N = int(input())
A = list(map(int,input().split()))

cnt = Counter(A)
rect = []

for i,j in zip(cnt.keys(),cnt.values()):
    if j >= 2:
        rect.append([i,j])

rect.sort(reverse=True)
##print(rect)
ans = 0
flag = False
finished = False
for i,j in rect:
    if flag:
        ans *= i
        finished = True
        break
    elif j < 4:
        ans = i
        flag = True
    else:
        ans = i**2
        finished = True
        break

print(0 if not finished else ans)

