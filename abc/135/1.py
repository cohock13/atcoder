def main():
    A,B = map(int,input().split())
    if ((A+B)/2)%1 != 0:
        print("IMPOSSIBLE")
    else:
        print(int((A+B)/2))


if __name__=="__main__":
    main()