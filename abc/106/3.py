S = input()
K = int(input())

ones = 0
nzero = ""
for i in S:
    if i == "1":
        ones += 1
    else:
        nzero = i
        break

if K <= ones:
    print(1)
else:
    print(nzero)


    