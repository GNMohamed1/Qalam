import ply.yacc as yacc
from toks import Token

class Parser:
    def __init__(self, vars):
        self.tokens = Token.tokens
        self.parser = None
        
        self.precedence = (
        ('left', 'OR'),
        ('left', 'AND'),
        ('right', 'NOT'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE'),
        ('right', 'POWER')
        )
        
        self.vars = vars
        
    def p_statement_assign(self, p):
        'statement : VAR IDENTIFIER ASSIGN expression'
        self.vars[p[2]] = p[4]
        p[0] = p[4]

    def p_statement_expr(self, p):
        'statement : expression'
        p[0] = p[1]

    def p_expression_plus(self, p):
        'expression : expression PLUS term'
        p[0] = p[1] + p[3]

    def p_expression_minus(self, p):
        'expression : expression MINUS term'
        p[0] = p[1] - p[3]

    def p_expression_term(self, p):
        'expression : term'
        p[0] = p[1]
        
    def p_expression_boolean(self, p):
        '''expression : BOOL'''
        p[0] = bool(p[1])

    def p_expression_not(self, p):
        'expression : NOT expression'
        p[0] = not p[2]

    def p_expression_and(self, p):
        'expression : expression AND expression'
        p[0] = p[1] and p[3]

    def p_expression_or(self, p):
        'expression : expression OR expression'
        p[0] = p[1] or p[3]

    def p_term_times(self, p):
        'term : term TIMES factor'
        p[0] = p[1] * p[3]

    def p_term_divide(self, p):
        'term : term DIVIDE factor'
        try:
            p[0] = p[1] / p[3]
        except ZeroDivisionError:
            print("division by zero!")
            p[0] = 0

    def p_term_factor(self, p):
        'term : factor'
        p[0] = p[1]
        
    def p_factor_power(self, p):
        'factor : factor POWER factor'
        p[0] = p[1] ** p[3]

    def p_factor_num(self, p):
        '''factor : INT
                  | FLOAT'''
        p[0] = p[1]

    def p_factor_identifier(self, p):
        'factor : IDENTIFIER'
        if p[1] in self.vars:
            p[0] = self.vars[p[1]]
        else:
            print(f"undefined variable '{p[1]}'")
            p[0] = 0

    def p_factor_group(self, p):
        'factor : LPAREN expression RPAREN'
        p[0] = p[2]

    def p_error(self, p):
        if p:
            print(f"syntax error at '{p.value}'")
        else:
            print("syntax error at EOF")

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)
