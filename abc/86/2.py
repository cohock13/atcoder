a,b = input().split()

s = int(a+b)
ans = "No"
for i in range(1,1000):
    if s/i == i:
        ans = "Yes"

print(ans)