A,B,X = (int(x) for x in input().split())

def buy(n):
    return A*n+B*len(str(n)) <= X

right = 1e9
left = 0

if A+B>X:
    ans = 0
elif A*(10**9)+B*10 <=X:
    ans = 10**9
else:
    while abs(right-left) > 1:
        m = int((right+left)/2)
        if buy(int(m)):
            left = m
        else:
            right = m
    ans = left

print(ans)