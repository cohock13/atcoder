p = 1
for i in range(1,int(input())+1):
    p = (p*i)%int(1e9+7)

print(p)