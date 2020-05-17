def sq(a):
    if a == 0:
        return "x"
    elif a == 1:
        return "."
    else:
        return "o"

a,b = map(int,input().split())
p = list(map(int,input().split()))
q = list(map(int,input().split()))

pin = [0]*11

for i in p:
    pin[i] = 1

for i in q:
    pin[i] = 2

print(sq(pin[7]),sq(pin[8]),sq(pin[9]),sq(pin[0]))
print(" "+sq(pin[4])+" "+sq(pin[5])+" "+sq(pin[6]))
print(" "*2+sq(pin[2])+" "+sq(pin[3]))
print(" "*3+sq(pin[1]))

