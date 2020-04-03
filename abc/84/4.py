MAX = 10**5 + 1
##下準備(素数判定)(https://python.ms/eratosthenes/#_1-%E7%B0%A1%E5%8D%98%E3%81%AA%E3%82%82%E3%81%AE)
def primes(n):
    is_prime = [1] * (n + 1)
    is_prime[0] = 0
    is_prime[1] = 0
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = 0
    return is_prime
a = primes(MAX)
prime = [0]*MAX
for i in range(1,MAX,2):
    if a[i] == 1 and a[int((i+1)/2)] == 1:
        prime[i] = 1
##下準備(累積和)
tmp = 0
csum = [0]*MAX
for i in range(MAX):
    if prime[i] == 1:
        tmp += 1
    csum[i] = tmp
csum.pop()

##入出力
Q = int(input())
lr = []
for i in range(Q):
    lr.append(list(map(int,input().split())))
for i in range(Q):
    print(csum[lr[i][1]]-csum[lr[i][0]-1])