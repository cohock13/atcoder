S = input()[::-1]

mods = [0]*2019
mods[0] += 1
f = 0
for i in range(len(S)):
    f = (f+pow(10,i,2019)*int(S[i]))%2019
    mods[f] += 1

print(sum([i*(i-1)//2 for i in mods]))