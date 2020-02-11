def main():
    n = int(input())
    p = list(map(int,input().split()))

    ans = 0

    for i in range(1,n-1):
        tmp = [p[i-1],p[i],p[i+1]]
        tmp.sort()
        if tmp[1] == p[i]:
            ans += 1
    
    print(ans)


if __name__=="__main__":
    main()