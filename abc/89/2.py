N = int(input())
S = list(input().split())

if len(set(S)) == 3:
    print("Three")
else:
    print("Four")