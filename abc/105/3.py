N = int(input())

if N == 0:
    print(0)
else:
    ans = ""
    while N != 0:
        digit = abs(N%(-2))##-2進法での桁数
        ans += str(digit)##桁追加
        N -= digit##引く
        N //= -2##これは何?
    print(ans[::-1])


        