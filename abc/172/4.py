N = int(input())
conv = [0]*(N+1)
for i in range(1,N+1):
    for j in range(1,N//i+1):##その数の倍数をメモ
        conv[i*j-1] += 1
   
##print(conv)
print(sum([(i+1)*conv[i] for i in range(N)]))