N = int(input())
a = list(map(int,input().split()))

b = sorted(zip(a,range(N)),reverse=True)

for _,i in b:
    print(i+1)