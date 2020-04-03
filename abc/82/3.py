N = int(input())
a = list(map(int,input().split()))

num = {}

for i in a:
    if i in num:
        num[i] += 1
    else:
        num[i] = 1

keys = list(num.keys())
values = list(num.values())

ans = 0
for i in range(len(keys)):
    if values[i] < keys[i]:
        ans += values[i]
    else:
        ans += values[i] - keys[i]

print(ans)