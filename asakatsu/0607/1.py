from collections import Counter
w = input()

c = Counter(w)

flag = True
for j in c.values():
    if (j%2) != 0:
        flag = False
    
if flag:
    print("Yes")
else:
    print("No")
