def main():
    N = int(input())
    S = input()
    f = S[0]
    count = 0

    for i in S:
        if i!=f:
            count+=1
        f = i

    print(count+1)


if __name__ == "__main__":
    main()