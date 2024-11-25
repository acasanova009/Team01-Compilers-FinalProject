
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BOOL COMMA EQ EQUAL FALSE GE GT ID IF INT LBRACE LE LPAREN LT MINUS NEQ NUMBER OR PLUS PRINT RBRACE RETURN RPAREN SEMICOLON STRING TIMES TRUEprogram : functionfunction : INT ID LPAREN RPAREN LBRACE block RETURN  NUMBER SEMICOLON RBRACEblock : block statementblock : emptystatement : INT ID EQUAL NUMBER SEMICOLONstatement : INT ID EQUAL simple_expression  SEMICOLONstatement : BOOL ID EQUAL simple_expression  SEMICOLONstatement : ID EQUAL NUMBER SEMICOLONstatement : ID EQUAL simple_expression SEMICOLONstatement : IF LPAREN logical_a RPAREN LBRACE block RBRACE statement : PRINT LPAREN term RPAREN SEMICOLONlogical_a : logical_a OR logical_blogical_a : logical_blogical_a : TRUE\n                 | FALSE\n                 | IDlogical_b : logical_b AND logical_clogical_b : logical_clogical_c : logical_c EQ logical_dlogical_c : logical_c NEQ logical_dlogical_c : logical_dlogical_d : logical_d LE marked_expressionlogical_d : logical_d GE marked_expressionlogical_d : logical_d LT marked_expressionlogical_d : logical_d GT marked_expressionmarked_expression : expressionlogical_d : marked_expressionsimple_expression : expressionexpression : expression PLUS termexpression : expression MINUS termexpression : termterm : term TIMES factorterm : factorfactor : NUMBERfactor : TRUEfactor : FALSEfactor : IDempty :'
    
_lr_action_items = {'INT':([0,7,8,9,13,47,48,64,65,69,70,79,80,81,],[3,-38,10,-4,-3,-8,-9,-5,-6,-7,-38,-11,10,-10,]),'$end':([1,2,52,],[0,-1,-2,]),'ID':([3,7,8,9,10,13,14,18,21,22,23,33,47,48,49,50,51,55,56,57,58,59,60,61,62,64,65,69,70,79,80,81,],[4,-38,11,-4,17,-3,20,24,38,24,24,24,-8,-9,24,24,24,24,24,24,24,24,24,24,24,-5,-6,-7,-38,-11,11,-10,]),'LPAREN':([4,15,16,],[5,21,22,]),'RPAREN':([5,24,28,29,30,31,34,35,36,37,38,39,40,41,42,43,44,66,67,68,71,72,73,74,75,76,77,78,],[6,-37,-31,-33,-35,-36,54,-13,-14,-15,-16,-18,-21,-27,-26,-34,63,-29,-30,-32,-12,-17,-19,-20,-22,-23,-24,-25,]),'LBRACE':([6,54,],[7,70,]),'RETURN':([7,8,9,13,47,48,64,65,69,79,81,],[-38,12,-4,-3,-8,-9,-5,-6,-7,-11,-10,]),'BOOL':([7,8,9,13,47,48,64,65,69,70,79,80,81,],[-38,14,-4,-3,-8,-9,-5,-6,-7,-38,-11,14,-10,]),'IF':([7,8,9,13,47,48,64,65,69,70,79,80,81,],[-38,15,-4,-3,-8,-9,-5,-6,-7,-38,-11,15,-10,]),'PRINT':([7,8,9,13,47,48,64,65,69,70,79,80,81,],[-38,16,-4,-3,-8,-9,-5,-6,-7,-38,-11,16,-10,]),'RBRACE':([9,13,32,47,48,64,65,69,70,79,80,81,],[-4,-3,52,-8,-9,-5,-6,-7,-38,-11,81,-10,]),'EQUAL':([11,17,20,],[18,23,33,]),'NUMBER':([12,18,21,22,23,33,49,50,51,55,56,57,58,59,60,61,62,],[19,25,43,43,45,43,43,43,43,43,43,43,43,43,43,43,43,]),'TRUE':([18,21,22,23,33,49,50,51,55,56,57,58,59,60,61,62,],[30,36,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'FALSE':([18,21,22,23,33,49,50,51,55,56,57,58,59,60,61,62,],[31,37,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'SEMICOLON':([19,24,25,26,27,28,29,30,31,43,45,46,53,63,66,67,68,],[32,-37,47,48,-28,-31,-33,-35,-36,-34,64,65,69,79,-29,-30,-32,]),'TIMES':([24,25,28,29,30,31,36,37,38,43,44,45,66,67,68,],[-37,-34,51,-33,-35,-36,-35,-36,-37,-34,51,-34,51,51,-32,]),'PLUS':([24,25,27,28,29,30,31,36,37,38,42,43,45,66,67,68,],[-37,-34,49,-31,-33,-35,-36,-35,-36,-37,49,-34,-34,-29,-30,-32,]),'MINUS':([24,25,27,28,29,30,31,36,37,38,42,43,45,66,67,68,],[-37,-34,50,-31,-33,-35,-36,-35,-36,-37,50,-34,-34,-29,-30,-32,]),'LE':([24,28,29,30,31,36,37,38,40,41,42,43,66,67,68,73,74,75,76,77,78,],[-37,-31,-33,-35,-36,-35,-36,-37,59,-27,-26,-34,-29,-30,-32,59,59,-22,-23,-24,-25,]),'GE':([24,28,29,30,31,36,37,38,40,41,42,43,66,67,68,73,74,75,76,77,78,],[-37,-31,-33,-35,-36,-35,-36,-37,60,-27,-26,-34,-29,-30,-32,60,60,-22,-23,-24,-25,]),'LT':([24,28,29,30,31,36,37,38,40,41,42,43,66,67,68,73,74,75,76,77,78,],[-37,-31,-33,-35,-36,-35,-36,-37,61,-27,-26,-34,-29,-30,-32,61,61,-22,-23,-24,-25,]),'GT':([24,28,29,30,31,36,37,38,40,41,42,43,66,67,68,73,74,75,76,77,78,],[-37,-31,-33,-35,-36,-35,-36,-37,62,-27,-26,-34,-29,-30,-32,62,62,-22,-23,-24,-25,]),'EQ':([24,28,29,30,31,36,37,38,39,40,41,42,43,66,67,68,72,73,74,75,76,77,78,],[-37,-31,-33,-35,-36,-35,-36,-37,57,-21,-27,-26,-34,-29,-30,-32,57,-19,-20,-22,-23,-24,-25,]),'NEQ':([24,28,29,30,31,36,37,38,39,40,41,42,43,66,67,68,72,73,74,75,76,77,78,],[-37,-31,-33,-35,-36,-35,-36,-37,58,-21,-27,-26,-34,-29,-30,-32,58,-19,-20,-22,-23,-24,-25,]),'AND':([24,28,29,30,31,35,36,37,38,39,40,41,42,43,66,67,68,71,72,73,74,75,76,77,78,],[-37,-31,-33,-35,-36,56,-35,-36,-37,-18,-21,-27,-26,-34,-29,-30,-32,56,-17,-19,-20,-22,-23,-24,-25,]),'OR':([24,28,29,30,31,34,35,36,37,38,39,40,41,42,43,66,67,68,71,72,73,74,75,76,77,78,],[-37,-31,-33,-35,-36,55,-13,-14,-15,-16,-18,-21,-27,-26,-34,-29,-30,-32,-12,-17,-19,-20,-22,-23,-24,-25,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'function':([0,],[2,]),'block':([7,70,],[8,80,]),'empty':([7,70,],[9,9,]),'statement':([8,80,],[13,13,]),'simple_expression':([18,23,33,],[26,46,53,]),'expression':([18,21,23,33,55,56,57,58,59,60,61,62,],[27,42,27,27,42,42,42,42,42,42,42,42,]),'term':([18,21,22,23,33,49,50,55,56,57,58,59,60,61,62,],[28,28,44,28,28,66,67,28,28,28,28,28,28,28,28,]),'factor':([18,21,22,23,33,49,50,51,55,56,57,58,59,60,61,62,],[29,29,29,29,29,29,29,68,29,29,29,29,29,29,29,29,]),'logical_a':([21,],[34,]),'logical_b':([21,55,],[35,71,]),'logical_c':([21,55,56,],[39,39,72,]),'logical_d':([21,55,56,57,58,],[40,40,40,73,74,]),'marked_expression':([21,55,56,57,58,59,60,61,62,],[41,41,41,41,41,75,76,77,78,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> function','program',1,'p_program_function','parser.py',131),
  ('function -> INT ID LPAREN RPAREN LBRACE block RETURN NUMBER SEMICOLON RBRACE','function',10,'p_function','parser.py',136),
  ('block -> block statement','block',2,'p_block','parser.py',141),
  ('block -> empty','block',1,'p_block_empty','parser.py',146),
  ('statement -> INT ID EQUAL NUMBER SEMICOLON','statement',5,'p_statement_variable_number','parser.py',153),
  ('statement -> INT ID EQUAL simple_expression SEMICOLON','statement',5,'p_statement_variable_expression','parser.py',168),
  ('statement -> BOOL ID EQUAL simple_expression SEMICOLON','statement',5,'p_statement_variable_bool','parser.py',183),
  ('statement -> ID EQUAL NUMBER SEMICOLON','statement',4,'p_statement_assignment_number','parser.py',205),
  ('statement -> ID EQUAL simple_expression SEMICOLON','statement',4,'p_statement_assignment_expression','parser.py',221),
  ('statement -> IF LPAREN logical_a RPAREN LBRACE block RBRACE','statement',7,'p_statement_if','parser.py',237),
  ('statement -> PRINT LPAREN term RPAREN SEMICOLON','statement',5,'p_statement_print','parser.py',244),
  ('logical_a -> logical_a OR logical_b','logical_a',3,'p_logical_or_binary','parser.py',253),
  ('logical_a -> logical_b','logical_a',1,'p_logical_or_direct','parser.py',265),
  ('logical_a -> TRUE','logical_a',1,'p_logical_or_unitary','parser.py',270),
  ('logical_a -> FALSE','logical_a',1,'p_logical_or_unitary','parser.py',271),
  ('logical_a -> ID','logical_a',1,'p_logical_or_unitary','parser.py',272),
  ('logical_b -> logical_b AND logical_c','logical_b',3,'p_logical_and','parser.py',284),
  ('logical_b -> logical_c','logical_b',1,'p_logical_and_direct','parser.py',296),
  ('logical_c -> logical_c EQ logical_d','logical_c',3,'p_comparator_equality','parser.py',303),
  ('logical_c -> logical_c NEQ logical_d','logical_c',3,'p_comparator_notequality','parser.py',310),
  ('logical_c -> logical_d','logical_c',1,'p_comparator_equality_direct','parser.py',316),
  ('logical_d -> logical_d LE marked_expression','logical_d',3,'p_relational_less_equal','parser.py',321),
  ('logical_d -> logical_d GE marked_expression','logical_d',3,'p_relational_greater_equal','parser.py',332),
  ('logical_d -> logical_d LT marked_expression','logical_d',3,'p_relational_less','parser.py',343),
  ('logical_d -> logical_d GT marked_expression','logical_d',3,'p_relational_greater','parser.py',354),
  ('marked_expression -> expression','marked_expression',1,'p_marked_expression','parser.py',364),
  ('logical_d -> marked_expression','logical_d',1,'p_relational_simple_direct','parser.py',370),
  ('simple_expression -> expression','simple_expression',1,'p_simple_expression','parser.py',375),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','parser.py',380),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','parser.py',395),
  ('expression -> term','expression',1,'p_expression_term','parser.py',409),
  ('term -> term TIMES factor','term',3,'p_term_times','parser.py',413),
  ('term -> factor','term',1,'p_term_factor','parser.py',428),
  ('factor -> NUMBER','factor',1,'p_factor_num','parser.py',435),
  ('factor -> TRUE','factor',1,'p_factor_true','parser.py',440),
  ('factor -> FALSE','factor',1,'p_factor_false','parser.py',445),
  ('factor -> ID','factor',1,'p_factor_variable','parser.py',451),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',457),
]
