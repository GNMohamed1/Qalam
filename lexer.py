import ply.lex as lex
from toks import Token


class Lexer:
    def __init__(self):
        self.tokens = Token.tokens
        self.lexer = None
        
    t_ignore = ' \t'
    t_PLUS    = r'\+'
    t_MINUS   = r'\-'
    t_TIMES   = r'\*'
    t_DIVIDE  = r'\/'
    t_LPAREN  = r'\('
    t_RPAREN  = r'\)'
    t_NUMBER  = r'\d+'


    def t_error(self, t):
        print(f"Illegal character '{t.value[0]}'")
        t.lexer.skip(1)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)