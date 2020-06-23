N = int(input())
days = [0]*6
for _ in range(N):
    b,a = map(float,input().split())
    if b >= 35:
        days[0] += 1
    if 30 <= b < 35:
        days[1] += 1
    if 25 <= b < 30:
        days[2] += 1
    if 25 <= a:
        days[3] += 1
    if a < 0 and 0 <= b:
        days[4] += 1
    if b < 0:
        days[5] += 1

print(*days) 