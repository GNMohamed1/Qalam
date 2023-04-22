import ply.lex as lex
from src.toks import Token


class Lexer:
    def __init__(self):
        self.tokens = Token.tokens
        self.vars = {}
        self.lexer = None
        
    t_ignore    = ' \t'
    t_PLUS      = r'\+'
    t_MINUS     = r'\-'
    t_TIMES     = r'\*'
    t_DIVIDE    = r'\/'
    t_POWER     = r'\*\*'
    t_LPAREN    = r'\('
    t_RPAREN    = r'\)'
    t_ASSIGN    = r'\='
    t_EQT       = r'\=\='
    t_NEQ       = r'\!\='
    t_LT        = r'\<'
    t_GT        = r'\>'
    t_ELT       = r'\<\='
    t_EGT       = r'\>\='
    t_SEMICOLON = r'\;'

    def t_IDENTIFIER(self, t):
        r'[a-zA-Z_\u0600-\u06FF][a-zA-Z0-9_\u0600-\u06FF]*'
        if t.value == 'متغير':
            t.type = 'VAR'
            return t
        
        if t.value == 'صح' or t.value == 'خطا':
            
            if t.value == 'صح':
                t.value = True
            else:
                t.value = False
            t.type = 'BOOL'
            return t
        
        if t.value == 'و':
            t.type = 'AND'
            return t
        
        if t.value == 'او':
            t.type = 'OR'
            return t
        
        if t.value == 'ليس':
            t.type = 'NOT'
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
    
    def t_NEWLINE(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)
        return t

    def t_error(self, t):
        print(f"Illegal character '{t.value[0]}'")
        t.lexer.skip(1)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        
if __name__ == "__main__":
    lexer = Lexer()
    lexer.build()
    lexer.lexer.input("متغير ا = 10 \n ا + 10 * 2")
    for token in lexer.lexer:
        print(token)
