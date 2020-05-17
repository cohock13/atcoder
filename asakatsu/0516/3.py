from collections import Counter

N = int(input())
A = list(map(int,input().split()))

c = Counter(A)

hen = []

for i,j in zip(c.keys(),c.values()):
    if 2 <= j <= 3:
        hen.append([i,2])
    elif j >= 4:
        hen.append([i,4])


hen.sort(reverse=True)

##print(hen)
ans = 0
finished = False
choosen = False

for i,j in hen:
    if j == 2:
        if choosen:
            ans *= i
            finished = True
            break
        else:
            ans = i
            choosen = True
    else:
        if choosen:
            ans *= i
            finished = True
            break
        else:
            ans = i**2
            finished = True
            break

print(ans if finished else 0)
