def is_beautiful(s):

    b = [0]*30

    for i in s:
        b[ord(i)-97] += 1
    
    flag = True
    for i in b:
        if i%2 != 0:
            flag = False
    
    return flag


print("Yes" if is_beautiful(input()) else "No")