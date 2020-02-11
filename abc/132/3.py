def main():
    import math
    N = int(input())
    d = list(map(int,input().split()))
    d.sort()
    mid = int(math.ceil(N/2))
    print(d[mid]-d[mid-1])

if __name__=="__main__":
    main()