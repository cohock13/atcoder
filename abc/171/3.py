##10 -> n 進法変換,逆はint(num,base)
def base_10_to_n(X, n):
    if (int(X/n)):
        return base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)

ans = base_10_to_n(int(input()),26)

print(ans)


