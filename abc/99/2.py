a,b = map(int,input().split())

for i in range(1000):
    if i == b-a:
        print(i*(i+1)//2-b)
        break
