s = list(input())
s.sort()
t = list(input())
t.sort(reverse=True)
s_p =  "".join(s) 
t_p = "".join(t)
if s_p < t_p:
    print("Yes")
else:
    print("No")