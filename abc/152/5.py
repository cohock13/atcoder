def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def lcm(a, b):
    return (a * b)//gcd(a,b)

N = int(input())
A = list(map(int,input().split()))

lcm_a = 1

for i in A:
    lcm_a = lcm(lcm_a,i)

ans = 0
for i in A:
    ans +=lcm_a//i 
    
mod = int(1e9+7)
print(ans%mod)




