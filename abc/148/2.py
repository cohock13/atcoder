N = int(input())
S,T = input().split()

num_s = 0
num_t = 0
for i in range(2*N):
    if i%2 == 0:
        c = S[num_s]
        print(c,end="")
        num_s += 1
    else:
        c = T[num_t]
        print(c,end="")
        num_t += 1