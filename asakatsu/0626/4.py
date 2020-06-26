S = input()
T = input()

if len(S) < len(T):
    print("UNRESTORABLE")
    exit()

##一つ一つパターンマッチさせる

ls = len(S)
lt = len(T)
index = -1
for i in range(ls-lt+1):
    cnd = S[i:i+lt]
    flag = True
    for s,t in zip(cnd,T):
        if s != "?":
            if s != t:
                flag = False
                break

    if flag:
        index = i


if index == -1:
    print("UNRESTORABLE") 
else:
    tmp = S.replace("?","a")
    print(tmp[:index]+T+tmp[index+lt:])