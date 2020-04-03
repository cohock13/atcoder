
##入力部
H,W,K = map(int,input().split())
S = []
for i in range(H):
    S.append([int(j) for j in input()])

def solve(n):

def main():
    ##分割する必要がない場合
    if sum(sum(l) for l in S) <= K:
        print(0)
        exit()
    ##横の場合を全探索
    ans = 1e10
    for i in range(2**(H-1)):
        ans = min(ans,solve(i))
    print(ans)

if __name__ == "__main__":
    main()