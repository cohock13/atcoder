N = int(input())
A = list(map(int,input().split()))

ans ="YES" if len(set(A))==N else "NO"

print(ans)