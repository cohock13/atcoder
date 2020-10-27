class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


N,M = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

uf = UnionFind(N)
for _ in range(M):
    q,p = map(int,input().split())
    uf.union(q-1,p-1)

flag = True
print(len(set(uf.par)))
aa = [0]*(N+10)
bb = [0]*(N+10)
for i,j in enumerate(uf.par):
    print(i,j)
    aa[j] += a[i-1]
    bb[j] += b[i-1]
print(aa,bb)
print("Yes" if aa == bb else "No")
