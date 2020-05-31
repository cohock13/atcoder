N = int(input())
pop = 0
town = []
for _ in range(N):
    s,p = input().split()
    town.append([s,int(p)])
    pop += int(p)

flag = False
name = ""
for i,j in town:
    if j > pop/2:
        flag = True
        name = i
    
print(name if flag else "atcoder")