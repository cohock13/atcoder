"""
　　　　　　　　 　 　 　 　 　 　 　 　 _ .:´:: :: :: :: :: :: :: :: : |
　　　 　 　 　 　 　 　 　 　 　 ,...＜ :: :: :: :: :: :: :: :: :: :: :: ::|
　　　　　　　　　　　　　　　／ : :: :: :: :: :: :: :: :: :: :: :: :: :: ::|
　　　　　　　　　　　　　　<:: :: :: ::_:: :: :: :: :: :: :: :: :: :: :: :: ::|
. 　,个 ､　　　　　　　　　　｀ヽ::／　＼:: :: :: :: :: :: :: :: :: :: ::|
　/　＼::＼＿　　　　　　　　 /　 ●　｀ー―　､:: :: :: :: :: ::|
　!　　　｀ヽ、:::ヽ 　 　 　 　 /| 、 　 　 　● 　 !:: :: :: :: :: ::|
　l /´＼　　＼:∧　　　 __ /::.ー― ､　　　　　 |:: :: :: :: :: : |
　丶 　　＼　　＼:.ー<´::／:: :: :: :: :: ＼＿＿.ノ:: :: :: :: :: :::|
　 　 ＼　　)　　 　 _＞<:: :: :: ／: :: :: :: :: :: :: ／´＼:: :: :: ﾉ
　　　　 ￣￣￣￣　　　｀ー'<＿_ノ: :: :: :: ／　　　　 ￣
　　　　　　　　　,ヘ ＿＿＿　　 <＿_ノ::/
　　　　　　　　　l:: :: :: :: :: :: ::｀ヽ ＿_/:::::l
　　 　 　 　 　 八:: :: :: :: :: :: :: :: :: :: :: :: :′
　　　　　　　　　　＼:: :: :: :: :: :: :: :: :: ::/
　　　　 　 　 　 　 　 ＼:: :: :: :: :: :: ::ノ
"""

##戦略
##塗られてない床まで移動し，塗る
##移動するのは[0，塗られてない一番右-R]まで

N,R = map(int,input().split())
S = input()
r = S[::-1].find(".")
S = list(S)
if (N-r)-R <= 0 or S.count("o") == N:
    if len(set(S)) == 1:##全部塗られてる
        print(0)
    else:##1回の塗りで済む
        print(1)
    exit()

ans = 0
i = 0
while i < (N-r)-R:
    if S[i] == ".":
        for j in range(R):
            S[min(i+j,N-1)] = "o"
    else:
        i += 1
    ans += 1

print(ans+1)