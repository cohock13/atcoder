from collections import defaultdict

N = int(input())

xy = [tuple(map(int,input().split())) for _ in range(N)]

tri = defaultdict(int)
ans = 0
for i in range(N):
    for j in range(i+1,N):
        for h in range(j+1,N):
            x,y = xy[i]
            x_1,y_1 = xy[j]
            x_2,y_2 = xy[h]

            S = abs(abs(x-x_1)*abs(y-y_2)-abs(x-x_2)*abs(y_1-y))

            if S%2 == 0 and S != 0:
                ans += 1

print(ans)