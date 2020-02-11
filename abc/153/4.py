H = int(input())

def hit_point(N):
    if N == 1:
        return 1
    else:
        return 2 * hit_point(N//2) + 1
        
print(hit_point(H))