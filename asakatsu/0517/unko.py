N,C,K = map(int,input().split())
T = sorted([int(input()) for _ in range(N)])

bus = 1
tmp_bus = 1
bus_time = T[0] + K

for t in T[1:]:

    if tmp_bus < C and t <= bus_time:
        tmp_bus += 1
    else:
        bus += 1
        bus_time = t + K
        tmp_bus = 1

print(bus)