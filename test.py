from sympy import symbols

from read import re
from lexer import Lexer, nonterminal
from lexer import TokenType
from lexer import Token
from lexer import nonterminal
from lexer import noToken
import math
import sympy

if __name__=="__main__":
    x = sympy.symbols("x")
    f=0.0+(x-x)
    print(f.evalf(subs={x:1}))