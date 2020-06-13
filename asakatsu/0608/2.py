X,Y = map(int,input().split())

a = [X]

for i in range(10000000):
    if a[-1]*2 <= Y:
        a.append(a[-1]*2)
    else:
        break

print(len(a))