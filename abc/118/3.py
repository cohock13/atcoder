N = int(input())
A = list(map(int,input().split()))

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

gcd_a = A[0]

for i in A:
    gcd_a = gcd(gcd_a,i)

print(gcd_a)
