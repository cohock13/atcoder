a = list(map(int,input().split()))

if len(set(a)) == 1:
    print(a[0])
    exit()

for i in a:
    if a.count(i) == 1:
        print(i)


