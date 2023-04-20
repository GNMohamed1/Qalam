import ply.yacc as yacc
from toks import Token

class Parser:
    def __init__(self):
        self.tokens = Token.tokens
        self.parser = None
        
        self.precedence = (
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE'),
        )

    def p_expression_plus(self, p):
        'expression : expression PLUS expression'
        p[0] = p[1] + p[3]

    def p_expression_minus(self, p):
        'expression : expression MINUS expression'
        p[0] = p[1] - p[3]

    def p_expression_times(self, p):
        'expression : expression TIMES expression'
        p[0] = p[1] * p[3]

    def p_expression_divide(self, p):
        'expression : expression DIVIDE expression'
        try:
            p[0] = p[1] / p[3]
        except ZeroDivisionError:
            print("division by zero!")
            p[0] = 0

    def p_expression_number(self, p):
        'expression : NUMBER'
        p[0] = int(p[1])

    def p_expression_group(self, p):
        'expression : LPAREN expression RPAREN'
        p[0] = p[2]

    def p_error(self, p):
        if p:
            print(f"syntax error at '{p.value}'")
        else:
            print("syntax error at EOF")

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)
