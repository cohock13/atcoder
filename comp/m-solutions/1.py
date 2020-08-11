X = int(input())

for i in range(2,11):
    if 200*i <= X <= 200*(i+1)-1:
        print(10-i)
        break