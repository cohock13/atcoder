n = int(input())

d = {}
for i in range(n):
    order,string = input().split()
    if order == "insert":
        d[string] = 1
    else:
        try:
            if d[string] :
                print("yes")
        except:
            print("no")
