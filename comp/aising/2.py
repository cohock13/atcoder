N = int(input())
a = list(map(int,input().split()))

print(sum(i%2 for i in a[::2]))