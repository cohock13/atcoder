s = input()

ans = []

for i in s:
    if i == "B":
        try:
            ans.pop()
        except:
            pass
    else:
        ans.append(i)
    
print("".join(ans))