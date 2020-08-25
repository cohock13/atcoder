N = input()

tmp = 0

for i in N:
    tmp += int(i)

if tmp%9 == 0:
    print("Yes")
else:
    print("No")