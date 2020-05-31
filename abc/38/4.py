from bisect import bisect_left
def min_search(a):

    b = [i for i in a if i != float("inf")]

    res = [b[0]]
    for i in range(len(b)):
        if b[i] > res[-1]:
            res.append(b[i])
        else:
            res[bisect_left(res,b[i])] = b[i]

    return len(res)

def max_search(a):

    b = [-i for i in a if i != 0]
    b = b[::-1]
    print(b)
    res = [b[0]]
    for i in range(len(b)):
        if b[i] > res[-1]:
            res.append(b[i])
        else:
            res[bisect_left(res,b[i])] = b[i]

    return len(res)

N = int(input())

w_first_max = [0 for _ in range(10**5+1)]
h_first_max = [0 for _ in range(10**5+1)]
w_first_min = [float("inf") for _ in range(10**5+1)]
h_first_min = [float("inf") for _ in range(10**5+1)]


for _ in range(N):
    w,h = map(int,input().split())
    w_first_max[h] = max(w_first_max[h],w)
    h_first_max[w] = max(h_first_max[w],h)
    w_first_min[h] = min(w_first_max[h],w)
    h_first_min[w] = min(h_first_max[w],h)

ans = 1
ans = max(ans,max_search(w_first_max),max_search(h_first_max))
ans = max(ans,min_search(w_first_min),min_search(h_first_min))
print(ans)