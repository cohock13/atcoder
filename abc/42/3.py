N,K = map(int,input().split())
D = list(input().split())


for i in range(N,100000):
    flag = True
    for n in str(i):
        if n in D:
            flag = False
            break
    if flag:
        print(i)
        break