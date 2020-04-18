S = list(input().split())
ans = []

for i in S:
    if i in ["+","-","*","/"]:
        a = ans.pop()
        b = ans.pop()
        ans.append(eval("b"+i+"a"))
    else:
        ans.append(int(i))

print(ans[0])