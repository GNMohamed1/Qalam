import ply.yacc as yacc
from src.toks import Token
from src.table  import SymbolTable

class Parser:
    def __init__(self, symbol_table:SymbolTable):
        self.symbol_table = symbol_table
        self.tokens = Token.tokens
        self.parser = None
        
        self.precedence = (
        ('left', 'OR'),
        ('left', 'AND'),
        ('right', 'NOT'),
        ('left',   'EQT'),
        ('left',   'NEQ'),
        ('left',   'LT'),
        ('left',   'GT'),
        ('left',   'ELT'),
        ('left',   'EGT'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE'),
        ('right', 'POWER')
        )
        
        
    def p_statement_assign(self, p):
        '''statement : VAR IDENTIFIER ASSIGN expression NEWLINE
                    | VAR IDENTIFIER ASSIGN expression
                    |  expression NEWLINE
                    | NEWLINE'''
        self.symbol_table.set_variable(p[2], p[4])
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
        
    def p_expression_eqt(self, p):
        'expression : expression EQT expression'
        p[0] = p[1] == p[3]
    
    def p_expression_neq(self, p):
        'expression : expression NEQ expression'
        p[0] = p[1] != p[3]
        
    def p_expression_lt(self, p):
        'expression : expression LT expression'
        p[0] = p[1] < p[3]
        
    def p_expression_gt(self, p):
        'expression : expression GT expression'
        p[0] = p[1] > p[3]
    
    def p_expression_elt(self, p):
        'expression : expression ELT expression'
        p[0] = p[1] <= p[3]
        
    def p_expression_egt(self, p):
        'expression : expression EGT expression'
        p[0] = p[1] >= p[3]

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
                  | FLOAT
                  | MINUS INT
                  | MINUS FLOAT'''
                  
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = -p[2]

    def p_factor_identifier(self, p):
        '''factor : IDENTIFIER
                | NEWLINE IDENTIFIER'''
        if self.symbol_table.is_variable(p[1]):
            p[0] = self.symbol_table.get_variable(p[1])
        else:
            print(f"undefined variable '{p[1]}'")
            p[0] = 0

    def p_factor_group(self, p):
        'factor : LPAREN expression RPAREN'
        p[0] = p[2]

    def p_error(self, p):
        if p:
            print(f"Syntax error at line {p.lineno}, position {p.lexpos}: unexpected token '{p.value}'")
        else:
            print("Syntax error at EOF")

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)
