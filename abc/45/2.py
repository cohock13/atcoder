from collections import deque

A = deque(list(input())+["e"])
B = deque(list(input())+["e"])
C = deque(list(input())+["e"])

turn = "a"

while turn != "e":

    if turn == "a":
        turn = A.popleft()
        if turn == "e":
            print("A")
            break
    elif turn == "b":
        turn = B.popleft()
        if turn == "e":
            print("B")
            break
    else:
        turn = C.popleft()
        if turn == "e":
            print("C")
            break
