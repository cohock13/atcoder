def main():
    N = int(input())
    Up = list(map(int,input().split()))
    Down = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        tmp = sum(Up[:i+1]) + sum(Down[i:])
        ans = max(ans,tmp)
    
    print(ans)

if __name__ == "__main__":
    main()