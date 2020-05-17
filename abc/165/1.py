K = int(input())
A,B = map(int,input().split())

tmp = K
for i in range(100000):
    if A <= tmp <= B:
        print("OK")
        break
    else:
        tmp += K
    
    if tmp > B:
        print("NG")
        break