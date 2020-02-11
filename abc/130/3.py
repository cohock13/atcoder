def main():
    W,H,x,y = map(int,input().split())
    ans = W*H/2
    split = 0
    if x == W/2 and y == H/2:
        split = 1
    print(ans)
    print(split)    


if __name__=="__main__":
    main()