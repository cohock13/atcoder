gender = {"Male":0,"Female":1}

N = int(input())

print(0)
left_str = input()
if left_str == "Vacant":
    exit()
print(N-1)
right_str = input()
if right_str == "Vacant":
    exit()

left = 0
right = N-1

for i in range(20):
    mid = (left+right)//2

    print(mid)
    mid_s = input()

    if mid_s == "Vacant":
        exit()

    if gender[mid_s] == (gender[left_str]+mid)%2:##正しい周期
        left = mid
    else:
        right = mid

    