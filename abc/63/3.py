N = int(input())
s = [int(input()) for _ in range(N)]

if sum(s)%10 != 0:
    print(sum(s))
else:
    ans = sum(s)
    s.sort()
    for i in s:
        ans -= i
        if ans%10 != 0:
            print(ans)
            exit()
        ans += i
    print(0)