day = {"1":31,"2":28,"3":31,"4":30,"5":31,"6":30,"7":31,"8":31,"9":30,"10":31,"11":30,"12":31}
a,b  = [int(x) for x in input().split()]
c,d  = [int(x) for x in input().split()]
if c-a == 1:
    print("1")
else:
    print("0")