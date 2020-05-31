A,B = map(int,input().split())

if A == 1:
    A += 13
if B == 1:
    B += 13

if A == B:
    print("Draw")
elif A < B:
    print("Bob")
else:
    print("Alice")