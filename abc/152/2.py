a,b = input().split()

ac = ""
bc = ""

for i in range(int(a)):
    bc += b

for i in range(int(b)):
    ac += a

ans = [ac,bc]

ans.sort()

print(ans[0])



