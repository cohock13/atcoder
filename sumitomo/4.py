import itertools

N = int(input())
S = input()
L = list(S)
count = 0

for i in range(0,1000):

    fst = 0
    snd = 0
    thd = 0
    tmp = 0

    if(i<10):
        num = "00"+str(i)
    elif(i<100):
        num = "0"+str(i)
    else:
        num = str(i)

    if num[0] in L:
        fst = L.index(num[0]) + 1
        tmp += 1
    if num[1] in L[fst:]:
        snd = fst + L[fst:].index(num[1]) + 1
        tmp += 1
    if num[2] in L[snd:]:
        thd = snd + L[snd:].index(num[2]) + 1
        tmp += 1
    if tmp == 3:
        count+= 1
        


print(count)
    
    

