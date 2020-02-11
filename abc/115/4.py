def burger(N):
    if N == 0:
        return "P"
    else:
        return "B" + burger(N-1) + "P" + burger(N-1) + "B"


N,K = map(int,input().split())
s = burger(N)
l = len(s)
s = s[l-K:]
print(s.count("P"))