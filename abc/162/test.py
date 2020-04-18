from operator import itemgetter
N = int(input())
A = list(map(int,input().split()))

odd = A[::2]
even = A[1::2]
csum_odd = []
csum_even = []
for i in range(2):
    csum_odd.append(odd[0])
    csum_even.append(even[1])
for i in range(len(odd)-1):
    odd[i+1] += odd[i]
    for j in range(2):
        csum_odd.append(odd[i+1])

for i in range(len(even)-1):
    even[i+1] += even[i]
    for j in range(2):
        csum_even.append(even[i+1])
print(csum_odd)
print(csum_even)
ans = -1e20
for i in range(N):
    ans = max(ans,csum_even[i]+csum_odd[-1]-csum_odd[i])

print(ans)




        