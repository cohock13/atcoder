N = int(input())

x = 1
for i in range(10):
    if x*2 <= N:
        x *= 2
    else:
        break

print(x)