N = int(input())

def ans(s):
    if int(s) > N:##Nより大きかったら終了
        return 0
    else:
        cnt = int(s.count("7") > 0 and s.count("5") > 0 and s.count("3") > 0) ##753数であるかどうか
        return ans(s+"3") + ans(s+"5") + ans(s+"7") + cnt ##その数に3,5,7をつけて753数になるものの数
    
print(ans("0"))##最初の状態は空文字ではなく0.一桁で753数になるものはないため