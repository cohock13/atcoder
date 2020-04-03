N = int(input())
A = list(map(int,input().split()))
ans = 0
process = []

def cumsum(reverse=False):
    global A,ans,process
    if reverse == False:
        for i in range(len(A)-1):
            A[i+1] += A[i]
            ans += 1
            process.append([i+1,i+2])
    else:
        for i in reversed(range(len(A)-1)):
            A[i-1] += A[i]
            ans += 1
            process.append([i+2,i+1])

def addmax():
    global A,ans,process
    ind = A.index(max(A))
    m = max(A)
    for i in range(N):
        A[i] += m
        ans += 1
        process.append([ind+1,i+1])

def addmin():
    global A,ans,process
    ind = A.index(min(A))
    m = min(A)
    for i in range(N):
        A[i] += m
        ans += 1
        process.append([ind+1,i+1])

def main():
    global A,ans,process
    if max(A) <= 0:##すべての要素が0以下の場合
        cumsum(reverse=True)
    elif min(A) >= 0:##すべての要素が0以上の場合
        cumsum()
    else:##正、負が両方ある場合
        if -1*min(A) < max(A):##最大値を足すほうが早い
            addmax()
            cumsum()
        else:##最小値を引くほうが畑井
            addmin()
            cumsum(reverse=True)
    ##出力
    print(ans)
    for i in range(ans):
        print(*process[i])

if __name__ == "__main__":
    main()