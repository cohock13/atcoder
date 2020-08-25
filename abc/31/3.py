N = int(input())
a = list(map(int,input().split()))


def f(n):
    array = None
    aoki = -1e9
    ##青木くんが一番得点を多く得られる場所を探す
    for i in range(N):
        if i != n:
            if i > n:
                tmp = a[n:i+1]
            else:
                tmp = a[i:n+1]
            
            point_aoki = sum(tmp[1::2])

            if point_aoki > aoki:
                aoki = point_aoki
                array = tmp
    ##その時の高橋くんの点数を計算
    ##print(array)
    takahashi = sum(array[::2])

    return takahashi

ans = -1e9
for i in range(N):
    ans = max(ans,f(i))

print(ans)