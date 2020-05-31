from collections import deque

S = input()[:12].replace("WB",":")
a = deque(list("::W:::W"))
sound = ["Do","Re","Mi","Fa","So","La","Si"]

for i in range(7):
    if ("".join(a)) == S:
        print(sound[i])
        exit()
    a.rotate(-1)


    
