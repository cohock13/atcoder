import math

def is_prime(n):
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

N = int(input())
ans = 0
for i in range(N):
    ans += int(is_prime(int(input())))

print(ans)