N = int(input())
a = list(map(int,input().split()))
num = 1
count = 0
for i in a:
    if i == num:
        num += 1
    else:
        count += 1

if count == N:
    print("-1")
else:
    print(count)



        

