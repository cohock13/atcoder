H,W = map(int,input().split())

m = ["#"*(W+2)]

for _ in range(H):
    m.append("#"+input()+"#")

m.append("#"*(W+2))

for i in m:
    print(i)