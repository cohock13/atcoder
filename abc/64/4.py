N = int(input())
S = input()

a = 0
b = 0

for i in S:
    if i == "(":
        a += 1
    else:
        if a <= 0:
            b += 1
        else:
            a -= 1

print("("*b+S+")"*a)