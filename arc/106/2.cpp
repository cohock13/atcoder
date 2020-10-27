#include <iostream>
#include <vector>
using namespace std;
using ll = long long;
 
 
struct UnionFind{
    vector<int> rnk, par, num;
    
    UnionFind(int N) : rnk(N), par(N), num(N){
        init();
    }
    void init(){
        for(int i = 0; i < rnk.size(); i++){
            rnk[i] = 0;
            par[i] = i;
            num[i] = 1;
        }
    }
    int find(int x){
        if(par[x] == x) return x;
        else return par[x] = find(par[x]);
    }
    void unite(int x, int y){
        x = find(x);
        y = find(y);
        if(x == y) return;
        if(rnk[x] < rnk[y]){
            par[x] = y;
            num[y] += num[x];
        }
        else{
            par[y] = x;
            num[x] += num[y];
            if(rnk[x] == rnk[y]) rnk[x]++;
        }
    }
    bool same(int x, int y){
        return (find(x) == find(y));
    }
    int size(int x){
        return num[find(x)];
    }
};
 
int main(){
    int n, m;
    scanf("%d %d", &n, &m);
    UnionFind tree(n);
	long a[n],b[n];
    for(int i = 0; i < n ; ++i){
      cin >> a[i];
    }
    for(int i = 0; i < n ; ++i){
      cin >> b[i];
    }
    while(m--){
        int u, v;
        scanf("%d %d",&u, &v);
        tree.unite(u-1,v-1);
		tree.unite(v-1,u-1);
    }
    long long aa[n],bb[n];
    for(int i = 0; i < n ; ++i){
      aa[i] = 0;
    }
    for(int i = 0; i < n ; ++i){
      bb[i] = 0;
    }
 
    for(int i = 0 ; i < n ; ++i){
      int tmp = tree.find(i);
      aa[tmp] += a[i];
      bb[tmp] += b[i];
    }
  
  bool flag = true;
    
    for(int i = 0 ; i < n ; ++i){
      if(aa[i] != bb[i]){
        flag = false;
      }
    }
  
  if(flag){
    cout << "Yes" << endl;
  }
  else{
    cout << "No" << endl;
  }
  return 0;
}