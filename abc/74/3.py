A,B,C,D,E,F = map(int,input().split())

MAX_SUGER = E*F/(E+100)


water = [min(A,B)*100,max(A,B)*100]
for i in range(1,31):
    for j in range(1,31):
        water.append(100*A*i+100*B*j)
water = sorted(list(set(water)))

suger = []
for i in range(101):
    for j in range(101):
        if C*i + D*j <= MAX_SUGER:
            suger.append(C*i+D*j)
suger = sorted(list(set(suger)))

ans = []
for s in suger:
    min_water = 100*s/E
    for w in water:
        if w >= min_water:
            ans.append([s/(w+s),w+s,s])
            break
ans.sort(reverse=True)

for c,w,s in ans:
    if w <= F:
        print(w,s)
        break
