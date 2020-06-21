def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def digits(n):
    s = str(n)
    res = 0
    for i in s:
        res += int(i)
    return res

n = int(input())

if n == 1:
    print("Not Prime")
    exit()

if is_prime(n):
    print("Prime")
else:
    if n%2 != 0 and n%10 != 5 and digits(n)%3 != 0:
        print("Prime")
    else:
        print("Not Prime")