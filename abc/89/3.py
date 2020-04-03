N = int(input())
name = {"M":0,"A":0,"R":0,"C":0,"H":0}
for i in range(N):
    tmp = input()
    f = tmp[0]
    if f in name:
        name[f] += 1

num = list(name.values())
ans = 0
for i in range(3):
    for j in range(i+1,4):
        for h in range(j+1,5):
            ans += num[i]*num[j]*num[h]

print(ans)