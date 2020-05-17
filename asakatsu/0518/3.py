N = int(input())
state = ["123456","234561","345612","456123","561234","612345"]
wat = (N//5)%6
rem = N%5

s = list(state[wat])

for i in range(rem):
    s[i],s[i+1] = s[i+1],s[i]

ans = ""

for i in s:
    ans += i

print(ans)


