N = input()
n = int(N)
h = int(N[0])

if h == 9:
    print(999)
else:
    if n > h * 111:
        h += 1
    print(h*111)