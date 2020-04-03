X,Y,A,B,C = map(int,input().split())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
r = list(map(int,input().split()))
p.sort(reverse=True)
p = p[:X]
q.sort(reverse=True)
q = q[:Y]

apples = []
for i in p:
    apples.append(i)
for j in q:
    apples.append(j)
for h in r:
    apples.append(h)

apples.sort(reverse=True)
print(sum(apples[:X+Y]))
"""
red = 0
green = 0
trans = 0
ans = 0
for i in range(A+B):
    num = apples[i][1]
    if num == 0 and red <= A:
        ans += apples[i][0]
        red += 1
    elif num == 1 and green <= B:
        ans += apples[i][0]
        green += 1
    elif num == 2 and trans <= C:
        ans += apples[i][0]
        if red < green:
            red += 1
        else:
            green += 1

print(ans)
"""    

