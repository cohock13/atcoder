MAX_COLORS = 8
DIFF_RATE = 400

def solve(a):

    colors = [0]*9

    for i in a:
        num = 0
        tmp = 400
        flag = True
        for j in range(9):
            if i < 0:
                flag = False
                break
            else:
                i -= 400
                num += 1
        if flag:
            colors[num-1] += 1
        else:
            colors[num-1] = 1
    print(colors)
    if sum(colors[:8]) == 0:
        print(1,colors[-1])
    else:
        print(sum(colors[:8]),sum(colors[:8])+colors[-1])

def main():
    N = int(input())
    a = list(map(int,input().split()))
    solve(a)

if __name__ == "__main__":
    main()