
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDrightNOTleftEQTleftNEQleftLTleftGTleftELTleftEGTleftPLUSMINUSleftTIMESDIVIDErightPOWERAND ASSIGN BOOL DIVIDE EGT ELT EQT FLOAT GT IDENTIFIER INT LPAREN LT MINUS NEQ NEWLINE NOT OR PLUS POWER RPAREN SEMICOLON TIMES VARstatement : VAR IDENTIFIER ASSIGN expression NEWLINE\n                    | VAR IDENTIFIER ASSIGN expression\n                    |  expression NEWLINE\n                    | NEWLINEstatement : expressionexpression : expression PLUS termexpression : expression MINUS termexpression : termexpression : BOOLexpression : NOT expressionexpression : expression AND expressionexpression : expression OR expressionexpression : expression EQT expressionexpression : expression NEQ expressionexpression : expression LT expressionexpression : expression GT expressionexpression : expression ELT expressionexpression : expression EGT expressionterm : term TIMES factorterm : term DIVIDE factorterm : factorfactor : factor POWER factorfactor : INT\n                  | FLOATfactor : IDENTIFIER\n                | NEWLINE IDENTIFIERfactor : LPAREN expression RPAREN'
    
_lr_action_items = {'VAR':([0,],[2,]),'NEWLINE':([0,3,4,6,7,8,9,10,11,12,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[5,-25,14,-8,-9,29,-21,-23,-24,29,29,29,29,29,29,29,29,29,29,29,-26,29,29,-10,29,29,-6,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-22,-27,48,]),'BOOL':([0,8,12,17,18,19,20,21,22,23,24,32,],[7,7,7,7,7,7,7,7,7,7,7,7,]),'NOT':([0,8,12,17,18,19,20,21,22,23,24,32,],[8,8,8,8,8,8,8,8,8,8,8,8,]),'INT':([0,8,12,15,16,17,18,19,20,21,22,23,24,26,27,30,32,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'FLOAT':([0,8,12,15,16,17,18,19,20,21,22,23,24,26,27,30,32,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'IDENTIFIER':([0,2,5,8,12,15,16,17,18,19,20,21,22,23,24,26,27,29,30,32,],[3,13,25,3,3,3,3,3,3,3,3,3,3,3,3,3,3,25,3,3,]),'LPAREN':([0,8,12,15,16,17,18,19,20,21,22,23,24,26,27,30,32,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'$end':([1,3,4,5,6,7,9,10,11,14,25,28,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,],[0,-25,-5,-4,-8,-9,-21,-23,-24,-3,-26,-10,-6,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-22,-27,-2,-1,]),'POWER':([3,9,10,11,25,43,44,45,46,],[-25,30,-23,-24,-26,30,30,30,-27,]),'TIMES':([3,6,9,10,11,25,33,34,43,44,45,46,],[-25,26,-21,-23,-24,-26,26,26,-19,-20,-22,-27,]),'DIVIDE':([3,6,9,10,11,25,33,34,43,44,45,46,],[-25,27,-21,-23,-24,-26,27,27,-19,-20,-22,-27,]),'PLUS':([3,4,6,7,9,10,11,25,28,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[-25,15,-8,-9,-21,-23,-24,-26,15,15,-6,-7,15,15,15,15,15,15,15,15,-19,-20,-22,-27,15,]),'MINUS':([3,4,6,7,9,10,11,25,28,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[-25,16,-8,-9,-21,-23,-24,-26,16,16,-6,-7,16,16,16,16,16,16,16,16,-19,-20,-22,-27,16,]),'AND':([3,4,6,7,9,10,11,25,28,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[-25,17,-8,-9,-21,-23,-24,-26,-10,17,-6,-7,-11,17,-13,-14,-15,-16,-17,-18,-19,-20,-22,-27,17,]),'OR':([3,4,6,7,9,10,11,25,28,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[-25,18,-8,-9,-21,-23,-24,-26,-10,18,-6,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-22,-27,18,]),'EQT':([3,4,6,7,9,10,11,25,28,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[-25,19,-8,-9,-21,-23,-24,-26,19,19,-6,-7,19,19,-13,-14,-15,-16,-17,-18,-19,-20,-22,-27,19,]),'NEQ':([3,4,6,7,9,10,11,25,28,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[-25,20,-8,-9,-21,-23,-24,-26,20,20,-6,-7,20,20,20,-14,-15,-16,-17,-18,-19,-20,-22,-27,20,]),'LT':([3,4,6,7,9,10,11,25,28,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[-25,21,-8,-9,-21,-23,-24,-26,21,21,-6,-7,21,21,21,21,-15,-16,-17,-18,-19,-20,-22,-27,21,]),'GT':([3,4,6,7,9,10,11,25,28,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[-25,22,-8,-9,-21,-23,-24,-26,22,22,-6,-7,22,22,22,22,22,-16,-17,-18,-19,-20,-22,-27,22,]),'ELT':([3,4,6,7,9,10,11,25,28,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[-25,23,-8,-9,-21,-23,-24,-26,23,23,-6,-7,23,23,23,23,23,23,-17,-18,-19,-20,-22,-27,23,]),'EGT':([3,4,6,7,9,10,11,25,28,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,],[-25,24,-8,-9,-21,-23,-24,-26,24,24,-6,-7,24,24,24,24,24,24,24,-18,-19,-20,-22,-27,24,]),'RPAREN':([3,6,7,9,10,11,25,28,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,],[-25,-8,-9,-21,-23,-24,-26,-10,46,-6,-7,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-22,-27,]),'ASSIGN':([13,],[32,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,8,12,17,18,19,20,21,22,23,24,32,],[4,28,31,35,36,37,38,39,40,41,42,47,]),'term':([0,8,12,15,16,17,18,19,20,21,22,23,24,32,],[6,6,6,33,34,6,6,6,6,6,6,6,6,6,]),'factor':([0,8,12,15,16,17,18,19,20,21,22,23,24,26,27,30,32,],[9,9,9,9,9,9,9,9,9,9,9,9,9,43,44,45,9,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> VAR IDENTIFIER ASSIGN expression NEWLINE','statement',5,'p_statement_assign','parse.py',28),
  ('statement -> VAR IDENTIFIER ASSIGN expression','statement',4,'p_statement_assign','parse.py',29),
  ('statement -> expression NEWLINE','statement',2,'p_statement_assign','parse.py',30),
  ('statement -> NEWLINE','statement',1,'p_statement_assign','parse.py',31),
  ('statement -> expression','statement',1,'p_statement_expr','parse.py',36),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','parse.py',40),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','parse.py',44),
  ('expression -> term','expression',1,'p_expression_term','parse.py',48),
  ('expression -> BOOL','expression',1,'p_expression_boolean','parse.py',52),
  ('expression -> NOT expression','expression',2,'p_expression_not','parse.py',56),
  ('expression -> expression AND expression','expression',3,'p_expression_and','parse.py',60),
  ('expression -> expression OR expression','expression',3,'p_expression_or','parse.py',64),
  ('expression -> expression EQT expression','expression',3,'p_expression_eqt','parse.py',68),
  ('expression -> expression NEQ expression','expression',3,'p_expression_neq','parse.py',72),
  ('expression -> expression LT expression','expression',3,'p_expression_lt','parse.py',76),
  ('expression -> expression GT expression','expression',3,'p_expression_gt','parse.py',80),
  ('expression -> expression ELT expression','expression',3,'p_expression_elt','parse.py',84),
  ('expression -> expression EGT expression','expression',3,'p_expression_egt','parse.py',88),
  ('term -> term TIMES factor','term',3,'p_term_times','parse.py',92),
  ('term -> term DIVIDE factor','term',3,'p_term_divide','parse.py',96),
  ('term -> factor','term',1,'p_term_factor','parse.py',104),
  ('factor -> factor POWER factor','factor',3,'p_factor_power','parse.py',108),
  ('factor -> INT','factor',1,'p_factor_num','parse.py',112),
  ('factor -> FLOAT','factor',1,'p_factor_num','parse.py',113),
  ('factor -> IDENTIFIER','factor',1,'p_factor_identifier','parse.py',117),
  ('factor -> NEWLINE IDENTIFIER','factor',2,'p_factor_identifier','parse.py',118),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_group','parse.py',126),
]