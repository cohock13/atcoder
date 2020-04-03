S = input()
T = input()

if len(T) > len(S):
    print("UNRESTORABLE")
else:
    ls = len(S)
    lt = len(T)
    for i in reversed(range(ls-lt+1)):
        tmp = S[i:i+lt]
        flag = True
        for j in range(lt):
            if tmp[j] != "?":
                if tmp[j] != T[j]:
                    flag = False
                    break
        if flag:
            ans = ""
            for h in range(i):
                if S[h] == "?":
                    ans += "a"
                else:
                    ans += S[h]
            ans += T
            for h in range(i+lt,ls):
                if S[h] == "?":
                    ans += "a"
                else:
                    ans += S[h]
            print(ans)
            exit()
    print("UNRESTORABLE")

