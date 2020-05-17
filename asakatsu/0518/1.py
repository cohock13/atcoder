A,B = map(int,input().split())
A = abs(A)
B = abs(B)
if A == B:
    print("Draw")
elif abs(A) < abs(B):
    print("Ant")
else:
    print("Bug")