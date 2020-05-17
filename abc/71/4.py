N = int(input())
s = input()
t = input()

mod = int(1e9)+7

ans = 1
bef = 0
i = 0
while i < N:
    ##print(bef,ans,i)
    if bef == 0:##最初
        if s[i] == t[i]:##たてならべ
            bef = 1
            ans *= 3
        else:
            bef = 2
            ans *= 6
            i += 1
    elif bef == 1:##前がたてならべ
        if s[i] == t[i]:
            ans = (ans*2)%mod
        else:
            bef = 2
            ans = (ans*2)%mod
            i += 1
    else:##前がよこならべ
        if s[i] == t[i]:
            bef = 1
        else:
            ans = (ans*3)%mod
            i += 1
    i += 1

print(ans%mod)