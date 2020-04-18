input()
a = set(list(map(int,input().split())))
input()
b = set(list(map(int,input().split())))

for i in sorted(a^b):
    print(i)