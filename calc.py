def sum(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def etc(a,b):
    return a%b
   
What = input("1.덧셈\n 2.뺄셈\n 3.나눗셈\n 4.곱셈\n 5.나머지\n")

if What == "1":
    fir,sec = input("수식을 입력하세요 ex)2+7\n").split("+")
    print(sum(int(fir),int(sec)))
    
elif What == "2":
    fir,sec = input("수식을 입력하세요 ex)2-7\n").split("-")
    print(sub(int(fir),int(sec)))
elif What == "3":
    fir,sec = input("수식을 입력하세요 ex)2/7\n").split("/")
    print(div(int(fir),int(sec)))
elif What == "4":
    fir,sec = input("수식을 입력하세요 ex)2*7\n").split("*")
    print(mul(int(fir),int(sec)))
elif What == "5":
    fir,sec = input("수식을 입력하세요 ex)2%7\n").split("%")
    print(etc(int(fir),int(sec)))
        
else:
    print(" 1~5중에서 선택하세염")

        
