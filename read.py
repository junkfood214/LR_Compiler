import json
from lexer import Token
from lexer import TokenType
from lexer import nonterminal
def re():
    with open('LR(1).json', 'r') as load_obj:
        a = json.load(load_obj)
        a = {tuple(eval(k)): a[k] for k in a}

    read_dic = dict()
    for i in a:
        key = list(i)
        key[1] = eval(key[1])
        read_dic[tuple(key)] = a[i]
    return read_dic
    
if __name__ == "__main__":
        re_dic=re()
        print(re_dic[(0,TokenType.FOR)])
