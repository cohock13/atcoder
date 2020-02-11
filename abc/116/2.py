def collaz(n):
    if n%2 == 0:
        return n//2
    else:
        return int(3*n+1)

s = int(input())

box = [-1]*(int(1e6+1))

box[s] = 1

i = 1

while 1:
    if box[collaz(s)] == 1:
        print(i+1)
        break
    else:
        box[collaz(s)] = 1
        s = collaz(s)
        i += 1
    