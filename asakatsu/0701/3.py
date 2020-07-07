N = int(input())
a = list(map(int,input().split()))

b = [(j,i+1) for i,j in enumerate(a)]

b.sort(reverse=True)

for _,n in b:
    print(n)