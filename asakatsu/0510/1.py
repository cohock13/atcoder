N,A,B = map(int,input().split())


a = N//(A+B)*A
b = N%(A+B)

print(a+min(A,b))