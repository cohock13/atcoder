input()
a = input().split()
input()
b = input().split()

A = ""
B = ""

for i in a:
    A += i
for i in b:
    B += i

if A < B:
    print(1)
else:
    print(0)

