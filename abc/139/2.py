A,B = map(int,input().split())

tap = 1
ans = 0

while True:
    if tap<B:
        tap += (A-1)
        ans += 1
    else:
        break

print(ans)

