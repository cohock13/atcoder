import math

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

N = int(input())

primes = []
mod = 1
count = 0
for i in range(2,55555+1):
    if i%5 == mod and is_prime(i):
        primes.append(i)
        count += 1
    if count == N:
        break

print(*primes)