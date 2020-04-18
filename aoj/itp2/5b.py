tmp = []
n = int(input())
for i in range(n):
    a,b,c,d,e = input().split()
    tmp.append([int(a),int(b),c,int(d),e])
tmp.sort()
for i in range(n):
    print(*tmp[i])