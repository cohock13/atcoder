#include<iostream>
#include<string>
using namespace std;

int main(void){
    
   string s;
   int ans;
   cin>>s;
   if(s=="SUN"){ans = 7;}
   else if(s=="SAT"){ans = 1;}
   else if(s=="MON"){ans = 6;}
   else if(s=="TUE"){ans = 5;}
   else if(s=="WED"){ans = 4;}
   else if(s=="THU"){ans = 3;}
   else if(s=="FRI"){ans = 2;}
   cout<<ans<<endl;
   return 0;
}