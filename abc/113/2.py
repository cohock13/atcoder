N = int(input())
T,A = map(int,input().split())
H = list(map(int,input().split()))

for i in range(N):
    H[i] = abs(A - (T - 0.006*H[i]))

print(H.index(min(H))+1)
