def main():
    def gcd(a,b):
        while b!=0:
            a,b=b,a%b
        return a
    def lcm(a, b):
        return (a * b)//gcd(a,b)
    def ans(N,C,D):
        return N-N//C-N//D+N//lcm(C,D)

    A,B,C,D = map(int,input().split())
    print(ans(B,C,D)-ans(A-1,C,D))
    
if __name__=="__main__":
    main()