def main():
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())
    
    ans = 0

    for i in range(A+1):
        for j in range(B+1):
            tmp = X - 500*i - 100*j
            if tmp >= 0 and tmp//50 <= C:
                ans += 1 
    print(ans)

if __name__ == "__main__":
    main()