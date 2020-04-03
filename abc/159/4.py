
N = int(input())
A = list(map(int,input().split()))

num = {}
for i in A:##O(N)
    if i not in num:
        num[i] = 1
    else:
        num[i] += 1


values = list(num.values())
keys = list(num.keys())
S = 0
for i in range(len(keys)):##O(N*2)
    if values[i] >= 2:
        S += values[i]*(values[i]-1)//2

for i in range(N):
    if num[A[i]] >= 3:
        print(S-num[A[i]]*(num[A[i]]-1)//2+(num[A[i]]-1)*(num[A[i]]-2)//2)
    elif num[A[i]] == 2:
        print(S-1)
    else:
        print(S)



    
