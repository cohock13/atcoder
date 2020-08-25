N,A,B = map(int,input().split())
pos = 0

def constrain(n):
    if A <= n <= B:
        return n
    elif A > n:
        return A
    else:
        return B

for _ in range(N):
    s,d = input().split()
    d = int(d)

    if s == "East":
        pos += constrain(d)
    else:
        pos -= constrain(d)

if pos == 0:
    print(pos)
elif pos < 0:
    print("West",-pos)
else:
    print("East",pos)