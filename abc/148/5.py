N = int(input())

ans = 0

if N%2 == 0:
    for i in range(100000000000):
        fact = 10 *(5 ** i)
        if fact<=N:
            ans+= (N//fact)
        else:
            break


print(int(ans))