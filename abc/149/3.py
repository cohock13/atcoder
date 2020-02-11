import math

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


X = int(input())

p = X
ans = 0
while True:
    if (is_prime(p)):
        ans = p
        break
    else:
        p += 1

print(ans)

    
