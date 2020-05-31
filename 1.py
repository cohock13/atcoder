"""
参考(真似させてもらいました)
https://atcoder.jp/contests/agc044/submissions/13546510
"""


##再帰する.割り切れないなら割り切れる近くの数について考える.
import sys
sys.setrecursionlimit(int(1e6))

def solve(N_,A,B,C,D):
    num = {}
    def saiki(N):
        ##なんであれN*Dは移動できる
        res = N*D
        if N == 0:
            return 0
        elif N == 1:
            return D
        if N in num:
            return num[N]
        
        if N%2 == 0:
            res = min(res,saiki(N//2)+A)
        else:##割り切れないとき,近い割り切れる数へと移動し,割り切る.
            res = min(res,saiki((N+1)//2)+A+D,saiki((N-1)//2)+A+D)
        
        if N%3 == 0:
            res = min(res,saiki(N//3)+B)
        else:
            res = min(res,saiki(N//3)+D*(N%3)+B,saiki(N//3+1)+D*(3-N%3)+B)
        
        if N%5 == 0:
            res = min(res,saiki(N//5)+C)
        else:
            res = min(res,saiki(N//5)+D*(N%5)+C,saiki(N//5+1)+D*(5-N%5)+C)
        
        ##メモ化
        num[N] = res

        return res
    
    print(saiki(N))

for _ in range(int(input())):
    N,A,B,C,D = map(int,input().split())
    solve(N,A,B,C,D)


