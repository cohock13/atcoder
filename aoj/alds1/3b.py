from collections import deque

time = 0
finished = 0
n,q = map(int,input().split())


def rotate(A):
    global time,finished
    b = A.popleft()
    if b[1] - q > 0:
        b[1] -= q
        time += q
        A.append(b)
    else:
        time += b[1]
        finished += 1
        print(b[0],time)


def main():    
    order = deque([])
    for _ in range(n):
        tmp = list(input().split())
        tmp[1] = int(tmp[1])
        order.append(tmp)

    ##print("-----")
    while finished < n:
        rotate(order)
    
if __name__ == "__main__":
    main()