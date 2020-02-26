n = int(input())
v = list(map(int,input().split()))

odd = []
even = []

if len(set(v)) == 1:
    print(n//2)
    exit()

for i in range(n):
    if i%2 == 0:
        even.append(v[i])
    else:
        odd.append(v[i])

box_e = [0]*int(1e5+1)
box_o = [0]*int(1e5+1)

for i in range(n//2):
    box_e[even[i]] += 1
    box_o[odd[i]] += 1

mode_e = box_e.index(max(box_e))
mode_o = box_o.index(max(box_o))
tmp_e = box_e
tmp_o = box_o
tmp_e.sort()
tmp_o.sort()
secmode_e = tmp_e[-2]
secmode_e = box_e.index(secmode_e)
secmode_o = tmp_o[-2]
secmode_o = box_o.index(secmode_o)
print(mode_e,secmode_e,mode_o,secmode_o)
ans = 0

if mode_e != mode_o:
    print("hoge")
    for i in range(n//2):
        if odd[i] != mode_o:
            ans += 1
        if even[i] != mode_e:
            ans += 1
    print(ans)
else:
    ans_1 = 0
    ans_2 = 0
    for i in range(n//2):
        if odd[i] != mode_o:
            ans_1 += 1
        if odd[i] != secmode_o:
            ans_2 += 1
        if even[i] != mode_e:
            ans_2 += 1
        if even[i] != secmode_e:
            ans_1 += 1
    print(min(ans_1,ans_2))
    

