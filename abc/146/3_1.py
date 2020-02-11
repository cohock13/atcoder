a,b,x = map(int,input().split())
 
tmp = 1
if a+b > x:
    print(0)

elif a**1e9+b*9 < x:
    ans = int(1e9)

else:
    for i in range(1,10):
        if a*(10**(i-1))+b*i <= x:
            digit = i
            break

print(int((x-b*ans)/a))