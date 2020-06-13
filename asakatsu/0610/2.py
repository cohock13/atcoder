S = list(input())

l = len(S)
for i in range(l):
    for j in range(i,l):
        tmp = S[:i] + S[j:]
        if "".join(tmp) == "keyence":
            print("YES")
            exit()
print("NO")