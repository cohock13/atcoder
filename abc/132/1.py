def main():
    from collections import Counter
    S = list(input())
    if len(Counter(S))==2:
        print("Yes")
    else:
        print("No")

    

if __name__=="__main__":
    main()
