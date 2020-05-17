N = int(input())
A = list(map(int,input().split()))
 
four = 0
two = 0
odd = 0
for i in A:
    if i%4 == 0:
        four += 1
    elif i%2 == 0:
        two += 1
    else:
        odd += 1
##2の塊との接続点が奇数であってはならない
if two >= 1:
    odd += 1
 
if odd <= four+1:
    print("Yes")
else:
    print("No")