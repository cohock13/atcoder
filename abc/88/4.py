"""
参考にさせていただきました.ありがとうございました.(https://atcoder.jp/contests/abc088/submissions/10819295)
"""

from collections import deque

def dfs(H,W,s):
    que = deque()
    que.append([0,0])##初期地点
    distance = [[-1 for i in range(W)] for j in range(H)]##距離を記録する配列
    dxdy = [[1,0],[0,1],[-1,0],[0,-1]]##縦横の4方向

    distance[0][0] = 1##今回は進んだ歩数が欲しいので1から始める

    flag = False ##ゴール(右下)についたかどうかのフラグ

    while que:##取り出せなくなるまでループ

        x,y = que.popleft()##現在地点

        if x == H-1 and y == W-1:##ゴールに到着
            flag = True
            break

        for i,j in dxdy:##4方向を走査
            dx = x + i
            dy = y + j
            if dx >= 0 and dx < H and dy >= 0 and dy < W and distance[dx][dy] == -1 and s[dx][dy] == ".":
                distance[dx][dy] = distance[x][y] + 1 ##値の更新(+1)
                que.append([dx,dy])##forループ後に移動した点を調べる

    if not flag:
        return -1
    else:
        ans = 0
        for i in range(H):
            ans += s[i].count("#")
        ##print("#",ans)
        ##print("dist",distance[-1][-1])
        return H*W - ans - distance[-1][-1]

def main():
    H,W = map(int,input().split())
    s = []
    for i in range(H):
        s.append(input())
    print(dfs(H,W,s))

if __name__ == "__main__":
    main()
