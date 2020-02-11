N,A,B = map(int,input().split())

ans = 0

if abs(A-B)%2 == 0:
    ans = abs(A-B)//2
elif (A-1)>(N-B):##Aのほうが端っこより遠い
    ans = N-B+1+(B-A-1)//2
else:##Bのほうが端っこより遠い
    A = N-A+1
    B = N-B
    ans = N-B+1+(B-A-1)//2

print(int(ans))