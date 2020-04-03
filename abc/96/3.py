H,W = map(int,input().split())
HW = []
for i in range(H+2):
    if i == 0 or i == H+1:
        HW.append(["."]*(W+1))
    else:
        HW.append(["."]+list(input())+["."])

for i in range(1,H):
    for j in range(1,W):
        if HW[i][j] == "#":
            if HW[i-1][j] == "#" or HW[i][j-1] == "#" or HW[i+1][j] == "#" or HW[i][j+1] == "#":
                continue
            else:
                print("No")
                exit()
print("Yes")



