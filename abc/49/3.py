S = input()

m = ["eraser","erase","dreamer","dream"]

for i in m:
    S = S.replace(i,"")


print("YES" if S == "" else "NO")