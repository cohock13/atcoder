
def res(n):
    if n == 0:
        return "x"
    elif n == 1:
        return "."
    else:
        return "o"


a,b = map(int,input().split())
p = list(map(int,input().split()))
q = list(map(int,input().split()))

s = [0]*10

for i in p:
    s[i] = 1

for i in q:
    s[i] = 2

pp = [res(i) for i in s]

print(pp[7],pp[8],pp[9],pp[0])
print(" "+pp[4],pp[5],pp[6])
print("  "+pp[2],pp[3])
print("   "+pp[1])