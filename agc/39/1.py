S = list(input())
K = int(input())
l = len(S)

if len(set(S)) == 1:
    print(l*K//2)
    exit()
else:
    ans = 0
    tmp = ""
    count = [1]
    for i in range(l-1):
        if S[i] == S[i+1]:
            count[-1] += 1
        else:
            count.append(1)
    
    for i in count:
        ans += i//2*K

    if S[0] == S[-1]:
        ans += K-1

    print(ans)




