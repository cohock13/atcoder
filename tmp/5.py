N = input()

if int(N[-1])%2 == 1:
    print(0)
else:
    N = int(N)
    ans = N//10
    for i in range(2,1000):
        tmp = 2*5**i
        if tmp > N:
            break
        else:
            ans += N//tmp
    print(ans)
