def main():
    N,X = map(int,input().split())
    L = list(map(int,input().split()))
    jump = [0]*(N**4)
    jump[0] = 1
    d = 0
    for i in range(N):
        d += L[i]
        jump[d] = 1
    
    print(sum(jump[:X+1]))
    


if __name__=="__main__":
    main()

#7m