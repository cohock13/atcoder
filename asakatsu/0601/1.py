N = int(input())
A = list(map(int,input().split()))

odd = sum(i%2 for i in A)
even = N-odd

if odd%2 == 1:
    print("NO")
else:
    print("YES")
