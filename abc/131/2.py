def main():
    N,L = map(int,input().split())
    taste = []

    for i in range(N):
        taste.append(L+i)
    
    pie = sum(taste)
    ans = 1e10
    ans = [0]*N

    for i in range(N):
        tmp = taste[i]
        taste[i] = 0
        ans[i] = abs(pie-sum(taste))
        taste[i] = tmp
    
    print(pie-taste[ans.index(min(ans))])




if __name__=="__main__":
    main()

#12m