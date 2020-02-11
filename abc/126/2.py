def yymm(x,y):
    if 1<=y and y<=12:
        return True
    else:
        return False

S = input()

x = int(S[:len(S)//2])
y = int(S[len(S)//2:])

if yymm(x,y) and yymm(y,x):
    print("AMBIGUOUS")
elif yymm(x,y):
    print("YYMM")
elif yymm(y,x):
    print("MMYY")
else:
    print("NA")