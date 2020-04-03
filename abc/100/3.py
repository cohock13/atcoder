def f(n):
    count = 0
    while n>1 and n%2==0:
        n/=2
        count += 1
    return count


N = int(input())
A = list(map(int,input().split()))

ans = list(f(i) for i in A)

print(sum(ans))
