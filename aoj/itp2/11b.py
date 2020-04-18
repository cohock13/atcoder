n = int(input())
d = list(map(int,input().split()))

for b in range(2**n):
    a = bin(b)[2:]
    a = a[::-1]
    ans = []
    for i in range(len(a)):
        if a[i] == "1":
            ans.append(i)
    ans.sort()
    flag = True
    for i in d[1:]:
        if i not in ans:
            flag = False
            break
    if flag:
        print(str(b)+":",*ans)
