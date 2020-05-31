n = int(input())
a = tuple(map(int,input().split()))

def check(mode):
    ans,s = 0,0
    if mode:##奇数番目が正
        for i in range(n):
            s += a[i]
            if i%2 == 0:
                if s <= 0:
                    ans += abs(s)+1
                    s = 1
            else:
                if s >= 0:
                    ans += abs(s)+1
                    s = -1
    else:
        for i in range(n):
            s += a[i]
            if i%2 == 0:
                if s >= 0:
                    ans += abs(s)+1
                    s = -1
            else:
                if s <= 0:
                    ans += abs(s)+1
                    s = 1
    return ans

print(min(check(True),check(False)))

