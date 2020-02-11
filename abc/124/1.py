A,B = map(int,input().split())

ans = 0

ans += max(A,B)

if A>B:
    A -= 1
else:
    B -= 1

ans += max(A,B)

print(ans)