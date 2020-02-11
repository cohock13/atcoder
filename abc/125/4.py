N = int(input())
A = list(map(int,input().split()))

B = []
ans = 0

for i in A:
    B.append(abs(i))

if N%2 == 0:
    ans = sum(B)
    
else:
    ans = sum(B) - min(B)

print(ans)
     

