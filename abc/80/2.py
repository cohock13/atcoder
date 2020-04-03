N = int(input())
S = str(N)
S = sum(list(int(i) for i in S))

if N%S == 0:
    print("Yes")
else:
    print("No")