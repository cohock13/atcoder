###https://juppy.hatenablog.com/entry/2019/03/26/%E8%9F%BB%E6%9C%AC_Python_%E4%BA%8C%E6%AC%A1%E5%85%83%E7%B4%AF%E7%A9%8D%E5%92%8C_%E7%AB%B6%E6%8A%80%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0_Atcoder
def da_generate(h,w,a):
    da = [[0]*w for j in range(h)]
    da[0][0] = a[0][0]
    for i in range(1,w):
        da[0][i] = da[0][i-1]+a[0][i]
    for i in range(1,h):
        cnt_w = 0
        for j in range(w):
            cnt_w += a[i][j]
            da[i][j] = da[i-1][j]+cnt_w
    return da

def count(H,W,S):
    count = 0
    for i in range(H):
        for j in range(W):
            count += S[i][j]
    return count

H,W,K = map(int,input().split())
S = []
for i in range(H):
    tmp = list(input())
    tmp2 = []
    for j in range(W):
        tmp2.append(int(tmp[j]))
    S.append(tmp2)
if count(H,W,S) <= K:
    print(0)
    exit()
rsum = da_generate(H,W,S)
m = rsum[-1][-1]
ind = 0
mid = 1e9
for i in range(H):
    for j in range(W):
        tmp = abs(m/2-rsum[i][j])
        if tmp < mid:
            ind = [i,j]
            mid = tmp
import math
import random
print(math.ceil(m/rsum[ind[0]][ind[1]]))
