xa = 0
bx = 0
ba = 0
ans = 0
N = int(input())

for _ in range(N):
    s = input()
    ans += s.count("AB")
    if s[0] == "B" and s[-1] == "A":
        ba += 1
    elif s[0] == "B":
        bx += 1
    elif s[-1] == "A":
        xa += 1

if xa == 0 and bx == 0 and ba != 0:
    print(ans+ba-1)
else:
    print(ans+min(xa,bx)+ba)