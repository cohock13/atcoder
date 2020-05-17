nums = []

for i in range(1,100):
    for j in range(2,100):
        nums.append(pow(i,j))
    
nums.sort(reverse=True)

X = int(input())

for i in nums:
    if i <= X:
        print(i)
        break