N = int(input())
R = []

for i in range(N):
    R.append(int(input()))

mins = [R[0]]
m = R[0]
for i in range(1,N):
    m = min(m,R[i])
    mins.append(m)

ans = -1e9
for i in range(1,N):
    ans = max(ans,R[i]-mins[i-1])

print(ans)
