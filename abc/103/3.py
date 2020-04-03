def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def lcm(a, b):
    return (a * b)//gcd(a,b)

N = int(input())
a = list(map(int,input().split()))

ans = 0
l = 1

for i in range(N):
    l = lcm(l,a[i])
l -= 1
for i in range(N):
    ans += l%a[i] 

print(ans)