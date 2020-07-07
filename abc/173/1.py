N = int(input())
if N%1000 == 0:
    print(0)
    exit()
print(1000-N%1000)