##幅優先探索
from collections import deque

def dfs(S,X,Y):
    que = deque()
    que.append([0,0,0,0])
    l = len(S)
    d = [[1,0],[0,1],[-1,0],[0,-1]]
    cd = [[1,3],[2,0],[3,1],[0,2]]

    while que:
        x,y,s,current_d = que.popleft()
        if s <= l-1:    
            if S[s] == "F":
                que.append([x+d[current_d][0],y+d[current_d][1],s+1,current_d])
            else:##S[s] == "T"
                for i in cd[current_d]:
                    que.append([x,y,s+1,i])
        else:
            if x == X and y == Y:
                return "Yes"
    return "No"

def main():
    s = input()
    x,y = map(int,input().split())
    print(dfs(s,x,y))

if __name__ == "__main__":
    main()

        