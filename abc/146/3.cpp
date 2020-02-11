#include<iostream>
#include<cmath>
using namespace std;

typedef long long ll;

ll A,B,X;

int get_digits (int n) {
	ll cnt = 0;
	while (n > 0) {
		n /= 10;
		cnt++;
	}
	return cnt;
}

bool can_buy(int n){
    return A*n+B*get_digits(n)<=X;
}

int main(void){
 ll ans;

 cin>>A>>B>>X;

 if(A+B>X){ans = 0;}
 else if(A*(1e9)+B*10<=X){ans = 1e9;}
 else{
     int ok = 0;
     int ng = 1e9;
     while(abs(ok-ng)>1){
         int mid = (int)(ok+ng)/2;
         if(can_buy(mid)){ok = mid;}
         else{ng = mid;}
     }
     ans = ok;
 }
 cout<<ans<<endl;
 }