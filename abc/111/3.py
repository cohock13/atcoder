from collections import Counter

def main():
    
    N = int(input())
    V = list(map(int,input().split()))
    odd = V[1::2]
    even = V[0::2]
    mode_o = Counter(odd).most_common()
    mode_o.append([0,0])
    mode_e = Counter(even).most_common()
    mode_e.append([0,0])
    ans = 0
    if mode_o[0][0] != mode_e[0][0]:
        ans = N-mode_o[0][1]-mode_e[0][1]
    else:
        ans = N - max(mode_e[0][1]+mode_o[1][1],mode_e[1][1]+mode_o[0][1])
    print(ans)

if __name__ == "__main__":
    main()