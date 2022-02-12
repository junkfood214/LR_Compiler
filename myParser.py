import math

import sympy
from sympy import symbols
from lexer import Lexer
from lexer import Token
from lexer import noToken
from lexer import nonterminal
from read import re


class parser:
    ve_st = [0]  # 状态栈
    ve_str = []  # 符号栈
    originstatement = [0, 0]
    ScaleStatement = [0, 0]
    RotStatement = [0]
    ForStatement = []
    statements = []
    grammer_switch = dict()
    LR_table = {}  # 分析表
    tokens = []  # 记号流
    line = 1

    def __init__(self):
        self.grammer_switch[0] = self.gra_0
        self.grammer_switch[1] = self.gra_1
        self.grammer_switch[2] = self.gra_2
        self.grammer_switch[3] = self.gra_3
        self.grammer_switch[4] = self.gra_4
        self.grammer_switch[5] = self.gra_5
        self.grammer_switch[6] = self.gra_6
        self.grammer_switch[7] = self.gra_7
        self.grammer_switch[8] = self.gra_8
        self.grammer_switch[9] = self.gra_9
        self.grammer_switch[10] = self.gra_10
        self.grammer_switch[11] = self.gra_11
        self.grammer_switch[12] = self.gra_12
        self.grammer_switch[13] = self.gra_13
        self.grammer_switch[14] = self.gra_14
        self.grammer_switch[15] = self.gra_15
        self.grammer_switch[16] = self.gra_16
        self.grammer_switch[17] = self.gra_17
        self.grammer_switch[18] = self.gra_18
        self.grammer_switch[19] = self.gra_19
        self.grammer_switch[20] = self.gra_20
        self.grammer_switch[21] = self.gra_21
        self.grammer_switch[22] = self.gra_22
        self.grammer_switch[23] = self.gra_23
        self.grammer_switch[24] = self.gra_24
        self.grammer_switch[25] = self.gra_25
        self.LR_table = re()

    def judge(self, str):  # 判断从字典中得到的下一步操作
        std = str[0]
        if std == 'S':
            return 1
        elif std == 'r':
            return 2
        elif std == 'a':
            return 3

    def shift(self, string):  # 移进函数
        sta = int(string[1:])
        self.ve_st.append(sta)
        self.ve_str.append(self.tokens[0])
        self.tokens.pop(0)

    def reduce(self, string):  # 规约函数
        order = int(string[1:])
        self.grammer(order)
        # print(self.ve_st)
        # for i in self.ve_str:
        #     try:
        #         print(i.tokenType)
        #     except:
        #         print(i.nonterminal)
        try:
            if type(self.ve_str[-1]) == Token:
                next = self.LR_table[(self.ve_st[-1], self.ve_str[-1].tokenType)]
            else:
                next = self.LR_table[(self.ve_st[-1], self.ve_str[-1].nonterminal)]
        except:
            raise Exception("错误规约,可能的原因:float divide by zero")
        # goto
        sta = int(next)
        self.ve_st.append(sta)

    def decision(self, string):
        self.tokens = Lexer(string)
        next = self.LR_table[(0, self.tokens[0].tokenType)]
        while self.tokens:
            # print(self.ve_st)
            # for i in self.ve_str:
            #     try:
            #         print(i.tokenType)
            #     except:
            #         print(i.nonterminal)
            try:
                next = self.LR_table[(self.ve_st[-1], self.tokens[0].tokenType)]
            except:
                raise Exception("语法错误,可能发生于" + "line:" + str(self.line) + "\n^" + str(self.tokens[0].lexeme) + "附近")
            ord = self.judge(next)
            if ord == 1:
                self.shift(next)
                continue
            elif ord == 2:
                self.reduce(next)
                continue
            elif ord == 3:
                print("语法分析结束")
                self.statements.append(self.originstatement)
                self.statements.append(self.ScaleStatement)
                self.statements.append(self.RotStatement)
                self.statements.append(self.ForStatement)
                self.gra_0()
                return self.statements

    def grammer(self, order):
        self.grammer_switch[order]()

    def gra_0(self):  # B-P

        self.ve_str.pop()
        self.ve_st.pop()
        self.ve_str.append(noToken(nonterminal.BEGIN, []))

    def gra_1(self):  # A-g
        con = self.ve_str.pop()
        self.ve_st.pop()
        temp = noToken(nonterminal.ATOM, [con.value])
        self.ve_str.append(temp)

    def gra_2(self):  # A-t
        self.ve_st.pop()
        self.ve_str.pop()
        t = symbols("T")
        self.ve_str.append(noToken(nonterminal.ATOM, [t]))

    def gra_3(self):  # A-u(E)
        self.ve_str.pop()
        e = self.ve_str.pop()
        self.ve_str.pop()
        f = self.ve_str.pop()
        self.ve_str.append(noToken(nonterminal.ATOM, [f.funcPtr(e.list[0])]))
        for i in range(4):
            self.ve_st.pop()

    def gra_4(self):  # A-(E)
        self.ve_str.pop()
        e = self.ve_str.pop()
        self.ve_str.pop()
        for i in range(3):
            self.ve_st.pop()
        self.ve_str.append(noToken(nonterminal.ATOM, [e.list[0]]))

    def gra_5(self):  # c-A@C
        c = self.ve_str.pop()
        self.ve_str.pop()
        a = self.ve_str.pop()
        self.ve_str.append(noToken(nonterminal.COMPONTENT, [a.list[0]**c.list[0]]))
        for i in range(3):
            self.ve_st.pop()

    def gra_6(self):  # c-a
        a = self.ve_str.pop()
        self.ve_st.pop()
        self.ve_str.append(noToken(nonterminal.COMPONTENT, [a.list[0]]))

    def gra_7(self):  # E-E+T
        t = self.ve_str.pop()
        self.ve_str.pop()
        e = self.ve_str.pop()
        self.ve_str.append(noToken(nonterminal.TERM, [e.list[0] + t.list[0]]))
        for i in range(3):
            self.ve_st.pop()

    def gra_8(self):  # E-E-T
        t = self.ve_str.pop()
        self.ve_str.pop()
        e = self.ve_str.pop()
        for i in range(3):
            self.ve_st.pop()
        self.ve_str.append(noToken(nonterminal.EXPRESSION, [e.list[0] - t.list[0]]))

    def gra_9(self):  # E-T
        t = self.ve_str.pop()
        self.ve_st.pop()
        self.ve_str.append(noToken(nonterminal.EXPRESSION, [t.list[0]]))

    def gra_10(self):
        '''
            F-ftaEbEcEd(E,E)
            ForStatment → FOR T
            FROM Expression
            TO Expression
            STEP Expression
            DRAW L_BRACKET Expression COMMA Expression R_BRACKET
        '''
        self.ve_str.pop()  # )
        e5 = self.ve_str.pop()  # e5
        self.ve_str.pop()  # ,
        e4 = self.ve_str.pop()  # e4
        self.ve_str.pop()  # (
        self.ve_str.pop()  # d
        e3 = self.ve_str.pop()  # e3
        self.ve_str.pop()  # c
        e2 = self.ve_str.pop()  # e2
        self.ve_str.pop()  # b
        e1 = self.ve_str.pop()  # e1
        for i in range(3):
            self.ve_str.pop()  # fta
        FOR = [e1.list[0], e2.list[0], e3.list[0], e4.list[0], e5.list[0]]

        self.ForStatement.append(FOR)

        self.ve_str.append(
            noToken(nonterminal.FORSTATEMENT, [e1.list[0], e2.list[0], e3.list[0], e4.list[0], e5.list[0]]))
        for i in range(14):
            self.ve_st.pop()

    def gra_11(self):  # G-+G
        g = self.ve_str.pop()
        self.ve_str.pop()
        for i in range(2):
            self.ve_st.pop()
        self.ve_str.append(g)

    def gra_12(self):  # G--G
        g = self.ve_str.pop()

        self.ve_str.pop()
        for i in range(2):
            self.ve_st.pop()
        self.ve_str.append(noToken(nonterminal.FACOR, [-g.list[0]]))

    def gra_13(self):  # G-C
        c = self.ve_str.pop()
        self.ve_st.pop()
        self.ve_str.append(noToken(nonterminal.FACOR, [c.list[0]]))

    def gra_14(self):  # O-op(E,E)
        self.ve_str.pop()  # )
        e2 = self.ve_str.pop()  # e2
        self.ve_str.pop()  # ,
        e1 = self.ve_str.pop()  # e1
        for i in range(3):  # op(
            self.ve_str.pop()
        for i in range(7):
            self.ve_st.pop()
        self.ve_str.append(noToken(nonterminal.ORIGINSTATEMENT, [e1.list[0], e2.list[0]]))
        self.originstatement[0] = e1.list[0]
        self.originstatement[1] = e2.list[0]

    def gra_15(self):  # P-S;P
        p = self.ve_str.pop()
        self.ve_str.pop()
        self.ve_str.pop()
        for i in range(3):
            self.ve_st.pop()
        self.ve_str.append(p)

    def gra_16(self):  # P-$
        self.ve_str.append(noToken(nonterminal.PROGRAM, []))

    def gra_17(self):  # R-rpE
        for i in range(3):
            self.ve_st.pop()
        e = self.ve_str.pop()
        for i in range(2):  # rp
            self.ve_str.pop()
        self.ve_str.append(noToken(nonterminal.ROTSTATEMENT, [e.list[0]]))
        self.RotStatement[0] = e.list[0]

    def gra_18(self):  # S-F
        self.line = self.line + 1
        f = self.ve_str.pop()
        self.ve_st.pop()
        self.ve_str.append(noToken(nonterminal.STATEMENT, f.list))

    def gra_19(self):  # S-O
        self.line = self.line + 1
        o = self.ve_str.pop()
        self.ve_st.pop()
        self.ve_str.append(noToken(nonterminal.STATEMENT, o.list))

    def gra_20(self):  # S-U
        self.line = self.line + 1
        u = self.ve_str.pop()
        self.ve_st.pop()
        self.ve_str.append(noToken(nonterminal.STATEMENT, u.list))

    def gra_21(self):  # S-R
        self.line = self.line + 1
        r = self.ve_str.pop()
        self.ve_st.pop()
        self.ve_str.append(noToken(nonterminal.STATEMENT, r.list))

    def gra_22(self):  # T-T*G
        g = self.ve_str.pop()
        self.ve_str.pop()
        t = self.ve_str.pop()
        self.ve_str.append(noToken(nonterminal.TERM, [g.list[0] * t.list[0]]))
        for i in range(3):
            self.ve_st.pop()

    def gra_23(self):  # T-T/G
        g = self.ve_str.pop()
        self.ve_str.pop()
        t = self.ve_str.pop()
        try:
            self.ve_str.append(noToken(nonterminal.TERM, [t.list[0] / g.list[0]]))
        except ZeroDivisionError:
            raise Exception(
                "语法错误,可能发生于" + "line:" + str(self.line) + "\n" + str(self.tokens[0].lexeme) + "附近发生float divide by "
                                                                                              "zero")
        for i in range(3):
            self.ve_st.pop()

    def gra_24(self):  # T-G
        g = self.ve_str.pop()
        self.ve_st.pop()
        self.ve_str.append(noToken(nonterminal.TERM, [g.list[0]]))

    def gra_25(self):  # U-qp(E,E)
        self.ve_str.pop()  # )
        e2 = self.ve_str.pop()  # e2
        self.ve_str.pop()  # ,
        e1 = self.ve_str.pop()  # e1
        for i in range(3):  # qp(
            self.ve_str.pop()
        for i in range(7):
            self.ve_st.pop()
        self.ve_str.append(noToken(nonterminal.SCALESTATEMENT, [e1.list[0], e2.list[0]]))
        self.ScaleStatement[0] = e1.list[0]
        self.ScaleStatement[1] = e2.list[0]


if __name__ == '__main__':
    string = '''
                origin is (100, 300);
                rot is pi/2;
                scale is (1, 1);
                for T from 0 to 200 step 1 draw (t, 0);
                for T from 0 to 150 step 1 draw (0, -t);
                for T from 0 to 120 step 1 draw (t, -2*t);
    '''
