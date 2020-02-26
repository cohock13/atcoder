#include<iostream>
using ll = long long;
using namespace std;

ll modpow(ll a, ll b, ll mod = 1000000007) {
   ll res = 1;
   for (a %= mod; b; a = a * a % mod, b >>= 1)
     if (b & 1) res = res * a % mod;
   return res;
 }

const int MAX = 1000;
const int MOD = 1000000007;

ll fac[MAX], finv[MAX], inv[MAX];

// テーブルを作る前処理
void COMinit() {
    fac[0] = fac[1] = 1;
    finv[0] = finv[1] = 1;
    inv[1] = 1;
    for (int i = 2; i < MAX; i++){
        fac[i] = fac[i - 1] * i % MOD;
        inv[i] = MOD - inv[MOD%i] * (MOD / i) % MOD;
        finv[i] = finv[i - 1] * inv[i] % MOD;
    }
}

// 二項係数計算
long long COM(int n, int k){
    if (n < k) return 0;
    if (n < 0 || k < 0) return 0;
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD;
}



 int main(void){
     ll a,b,n,A=0,B=0,S;
     cin>>n>>a>>b;
     S = modpow(2,n) -1;

     if(a<n+1){

         A = COM(n,a);
     }
     if(b<n+1){

         B = COM(n,b);
     }
     cout<<S-A-B;
     return 0;

 }