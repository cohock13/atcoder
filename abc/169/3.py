from decimal import Decimal

A,B = input().split()
A = int(A)
B = int(B[0]+B[2]+B[3])
C = A*B
print(C//100)



