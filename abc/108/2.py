import numpy as np

x1,y1,x2,y2 = map(int,input().split())

x1y1 = np.array([x1,y1])
x2y2 = np.array([x2,y2])

vector = x1y1 - x2y2
rotation = np.array([[0,1],
                     [-1,0]])
rotated_vector = np.dot(rotation,vector)
x3y3 = x2y2 + rotated_vector
x4y4 = x3y3 + vector

print(x3y3[0],x3y3[1],x4y4[0],x4y4[1])
print(*x3y3,*x4y4)##Python3.4だとこれはREになる