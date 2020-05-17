X = int(input())
C = 100
for i in range(100000):
    C += int(C*0.01)
    if C >= X:
        print(i+1)
        break