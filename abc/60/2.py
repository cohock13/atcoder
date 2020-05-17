A,B,C = map(int,input().split())

ans = []
for i in range(1,10000):
    ans.append((A*i)%B)

print("YES" if C in ans else "NO")