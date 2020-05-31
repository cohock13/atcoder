W,a,b = map(int,input().split())
if b <= a+W <= b+W:
    print(0)
else:
    print(min(abs(b-(a+W)),abs(a-(b+W))))