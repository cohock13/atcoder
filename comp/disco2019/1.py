X,Y = map(int,input().split())

prize = [0]*206
prize[1] = 300000
prize[2] = 200000
prize[3] = 100000

money = 0

if X == 1 and Y == 1:
    money += 400000

print(money+prize[X]+prize[Y])