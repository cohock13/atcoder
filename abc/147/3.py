def main():
    N = int(input())
    testimony = [[] for i in range(N)]
    for i in range(N):
        for j in range(int(input())):
            x,y = map(int,input().split())
            testimony[i].append([x-1,y])##0-indexに直す
    
    ans = 0
    for i in range(2**N):##証言について、2^N通り
        for j in range(N):##N人について検証
            flag = True
            if (i>>j)&1:##正直者である場合
                for x,y in testimony[j]:
                    if ((i>>x)&1) != y:##嘘をついている
                        flag = False
                        break
                if not flag:
                    break        
        if flag:##全員正直であった場合
            tmp = list(bin(i))
            ans = max(ans,tmp[2:].count("1"))

    print(ans)

if __name__ == "__main__":
    main()

    

