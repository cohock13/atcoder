
a,b,c = map(int,input().split())

if c - b - a <= 0:
    print("No")
elif 4*a*b < (c-b-a)**2:
    print("Yes")
else:
    print("No")