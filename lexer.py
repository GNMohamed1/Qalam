import ply.lex as lex
from toks import Token
from global_table import vars


class Lexer:
    def __init__(self):
        self.tokens = Token.tokens
        self.vars = vars
        self.lexer = None
        
    t_ignore = ' \t'
    t_PLUS    = r'\+'
    t_MINUS   = r'\-'
    t_TIMES   = r'\*'
    t_DIVIDE  = r'\/'
    t_POWER   = r'\*\*'
    t_LPAREN  = r'\('
    t_RPAREN  = r'\)'
    t_ASSIGN  = r'='
    t_VAR     = r'متغير'
    
    def t_IDENTIFIER(self, t):
        r'[a-zA-Z_\u0600-\u06FF][a-zA-Z0-9_\u0600-\u06FF]*'
        if t.value == 'متغير':
            t.type = 'VAR'
            return t
        t.type = 'IDENTIFIER'
        return t
    
    def t_FLOAT(self, t):
        r'\d+\.\d+'
        t.value = float(t.value)
        t.type = 'FLOAT'
        return t

    def t_INT(self, t):
        r'\d+'
        t.value = int(t.value)
        t.type = 'INT'
        return t



    def t_error(self, t):
        print(f"Illegal character '{t.value[0]}'")
        t.lexer.skip(1)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        
if __name__ == "__main__":
    lexer = Lexer()
    lexer.build()
    lexer.lexer.input("1")
    for token in lexer.lexer:
        print(token)
