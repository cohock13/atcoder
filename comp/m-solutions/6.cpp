#include<iostream>
using namespace std;
 
int main()
{
    long int t;
    cin>>t;
    while(t--)
    {
        long xe,ye;char de;
 
        cin>>xe>>ye>>de;
 
        int ch;
        map<char,char> rev;
 
        rev.clear();
 
        if(de=='L')
        {rev['U']='D';rev['D']='U';rev['L']='R';rev['R']='L';ch=1;}
        if(de=='D')
        {rev['U']='L';rev['L']='D';rev['D']='R';rev['R']='U';ch=2;}
        if(de=='U')
        {rev['U']='R';rev['R']='D';rev['D']='L';rev['L']='U';ch=3;}
        if(de=='R')
        {rev['U']='U';rev['R']='R';rev['D']='D';rev['L']='L';ch=4;}
 
 
 
        long n;cin>>n;
      //  cout<<'n';
 
        long double mn=100000;
        for(long i=0;i<n;i++)
        {
            long a,b,aa,bb;char d;
 
            cin>>aa>>bb>>d;
 
            aa-=xe;
            bb-=ye;
 
          //cout<<aa<<' '<<bb<<' '<<d<<' '<<ch<<endl;
            if(ch==1)
            {a=-aa;b=-bb;}
            if(ch==2)
            {a=-bb;b=aa;}
            if(ch==3)
            {a=bb;b=-aa;}
            if(ch==4) {a=aa;b=bb;}
 
            d=rev[d];
            //cout<<a<<' '<<b<<' '<<d<<endl;
 
            if(a<0||d=='R')continue;
           else if(b==0&&d=='L'){if(mn>(a*0.5))mn=(a*0.5);}
           else if(a==b&&d=='D'){if(mn>(a))mn=(a)*1.0;}
           else if(a==-b&&d=='U'){if(mn>(a))mn=(a)*1.0;}
 
        }
 
        if(mn<100000)
        {cout<<mn;
        if(fmod(mn,1)==0)cout<<".0";}
 
        else cout<<"SAFE";
cout<<endl;
 
        }
    return 0;
}