def main():
    N = int(input())
    H = list(map(int,input().split()))
    ans = "Yes"

    for i in reversed(range(N-1)):
        if H[i]>H[i+1]:
            H[i] -= 1
            if H[i]>H[i+1]:
                ans = "No"
                break
    print(ans)

if __name__ =="__main__":
    main()