import math
from collections import deque
def main():
    h,w,k = tuple([int(t)for t in input().split()])
    s = [list(input())for _ in range(h)]
    output = [[-1]*w for _ in range(h)]
 
    counter = 1
    for i,s_ in enumerate(s):
        if '#' in s_ :
            temp = 0
            for j,piece in enumerate(s_):
                output[i][j] = counter
                if piece == "#":
                    counter +=1
                    temp = j+1
                    
            if s_[w-1] != "#":
                counter -=1
                ##print(counter)
                output[i][temp:w] = [counter]*(w-temp)
 
        counter += 1
 
    for i in range(h-1):
        if not "#" in s[i+1]:
            output[i+1] = output[i]
    for i in range(1,h)[::-1]:
        if not "#" in s[i-1]:
            output[i-1] = output[i]
 
    for o_ in output:
        for o in o_:
            print(o,end=" ")
        print()
 
if __name__ == "__main__":
    main()