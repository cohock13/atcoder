N = int(input())
blue = []
red = []
for i in range(N):
    a,b = input().split()
    a = int(a)
    if b == "B":
        blue.append(a)
    else:
        red.append(a)
blue.sort()
red.sort()

for i in red:
    print(i)
for i in blue:
    print(i)
