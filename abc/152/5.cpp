#include<iostream>
using namespace std;

int gcd(int a, int b)
{
    if (a < b) {
        a ^= b;
        b ^= a;
        a ^= b;
    }
    
    return b ? gcd(b, a % b) : a;
}

int lcm(int a, int b)
{
    return a * b / gcd(a, b);
}

int main(void){
    long long N;
    cin>>N;
    long long A[N];
    for (int i = 0;i<N;++i){
        cin>>A[i];
    }
    long long a_lcm = 1;
    long long mod = 1e9 + 7;
    for (int i = 0;i<N;++i){
        a_lcm = lcm(a_lcm,A[i])%mod;
    }
    cout<<a_lcm;
    long long B=0;

    for (int i = 0;i<N;++i){
        B += (a_lcm/A[i]);
    }

    cout<<B%mod<<endl;
    return 0;
}