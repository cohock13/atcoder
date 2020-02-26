n = list(input())

ans = ""

for i in n:
    if i == "1":
        i = "9"
    elif i == "9":
        i = "1"
    ans += i

print(ans)