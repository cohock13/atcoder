N = int(input())
SP = []

for i in range(N):
    S,P = input().split()
    P = int(P)
    SP.append([S,-P,i+1])

SP.sort()

for i in range(N):
    print(SP[i][2])