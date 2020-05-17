N = int(input())
A = list(map(int,input().split()))

B = [abs(i) for i in A]
minus = [int(i<0) for i in A]
if sum(minus)%2 == 0:
    print(sum(B))
else:
    print(sum(B)-2*min(B))

