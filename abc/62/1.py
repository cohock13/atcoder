n = [0,1,0,2,0,2,0,0,2,0,2,0]
x,y = map(int,input().split())
print("Yes" if n[x-1] == n[y-1] else "No")