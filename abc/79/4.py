from scipy.sparse.csgraph import dijkstra
import numpy as np 

def main():
    H,W = map(int,input().split())
    graph = []
    for i in range(10):
        graph.append(list(map(int,input().split())))
    c = []
    for j in range(H):
        c.append(list(map(int,input().split())))

    dist = np.array(dijkstra(graph),dtype="int32")
    ans = 0
    for i in range(H):
        for j in c[i]:
            if j != -1:
                ans += dist[j][1] 
    print(ans)
if __name__ == "__main__":
    main()
    