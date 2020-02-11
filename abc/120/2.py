A,B,K = map(int,input().split())

a = []

for i in range(1,100000):
    if A%i == 0 and B%i == 0:
        a.append(i)

print(a[-K])
        


