import ply.yacc as yacc
from lexer import tokens

# Tabla de símbolos inicializada como un diccionario vacío
symbol_table = {}
#Postfijo
postfix = []

errorSemantic = 0
# Función para declarar una variable en la tabla de símbolos
def declare_variable(name, var_type, value):
    """
    Declara una nueva variable en la tabla de símbolos.
    Verifica si el nombre de la variable ya existe y, si no, lo agrega.
    """
    # Print the current symbol table for debugging
    #print(f"ANTES nueva var: :  <ID = expression>")

    #print(symbol_table)
    #print(f"-----------------")
    # Check if the variable is already declared
    if name in symbol_table:
        print(f"Error: The variable '{name}' is already declared.")
        return False  # Variable already declared

    # Add the variable with the specified type and value if type compatibility is met
    if (var_type == "int" and isinstance(value, int) and not isinstance(value, bool)) or \
       (var_type == "bool" and isinstance(value, bool)):
        symbol_table[name] = {'type': var_type, 'value': value}
        return True  # Variable successfully added
    
    # Type incompatibility error
    print(f"Error: Type mismatch for variable '{name}'. Expected {var_type}, got {type(value).__name__}.")
    return False  # Type incompatibility


# Función para asignar un valor a una variable existente en la tabla de símbolos
def assign_variable(name, value):
    """
    Asigna un valor a una variable existente en la tabla de símbolos.
    Verifica si el tipo de dato coincide con el tipo declarado de la variable.
    """

     # Print the current symbol table for debugging
    #print(f"ANTES asignar: :  <ID = expression>")

    #print(symbol_table)
    #print(f"-----------------")

    if name in symbol_table:
        # Verifica si el tipo del valor coincide con el tipo declarado
        var_type = symbol_table[name]['type']
        if (var_type == "int" and isinstance(value, int) and not isinstance(value, bool))or \
           (var_type == "bool" and isinstance(value, bool)):
            # Asigna el valor si el tipo es compatible
            symbol_table[name]['value'] = value
            #print(f"DESPUES asignar: :  <ID = expression>")
            
            #print(symbol_table)
            #print(f"-----------------")

            return True  # Asignación exitosa
               
        else:
            errorSemantic = 1
            print(f"Error: Tipo de dato incompatible para la variable '{name}'.")
            return False  # Error de tipo de dato
    else:
        print(f"Error: The variable '{name}' has not been declared.")
        return False  # La variable no existe

     
    # Print the current symbol table for debugging
    #print(f"Tabla de simbolos :")

    #print(symbol_table)
    #print(f"-----------------")

def get_variable_value(name):
    """
    Retorna el valor de la variable si está declarada en la tabla de símbolos.
    Si la variable no existe, muestra un mensaje de error.
    """
    if name in symbol_table:
        #print(f"The variable was read properly")
        return symbol_table[name]['value']
    else:
        print(f"Error: The variable '{name}' has not been declared.")
        return None


#---------------------------------SEMATICOS------------


def check_int_operands(op1, op2):
    """
    Verifica que ambos operandos sean del tipo `int` para operaciones aritméticas.
    Retorna True si ambos son `int`, False si no.
    """
    if isinstance(op1, int) and not isinstance(op1, bool) and \
       isinstance(op2, int) and not isinstance(op2, bool):
        return True
    else:
        print("Semantic error: Arithmetic operation requires integer types.")
        errorSemantic = 1
        return False
    

def check_bool_operands(op1, op2):
    """
    Verifica que ambos operandos sean del tipo `bool` para operaciones lógicas.
    Retorna True si ambos son `bool`, False si no.
    """
    
    if isinstance(op1, bool) and isinstance(op2, bool) :
        return True
    else:
        print("Error: Operación lógica requiere operandos de tipo bool.")
        errorSemantic = 1
        return False


#-----------------------------------


def p_program_function(p):
    'program : function'
    p[0] = p[1]


def p_function(p):
    'function : INT ID LPAREN RPAREN LBRACE block RETURN  NUMBER SEMICOLON RBRACE'
    p[0] = ('Function\n',p[1],p[2],p[3],p[4], p[5],p[6],p[7],p[8],p[9],p[10] )
    

def p_block(p):
    '''block : block statement'''
    
    p[0] = ('Block',p[1] ,p[2])

def p_block_empty(p):
    '''block : empty'''
    p[0] = ('Block',p[1])


# int a = 15;

def p_statement_variable_number(p):
    '''statement : INT ID EQUAL NUMBER SEMICOLON'''
    if isinstance(p[4], int):
        if declare_variable(p[2], "int", p[4]):
            p[0] = p[4]
            postfix.append(p[4])
            postfix.append(p[2])
            postfix.append('S')
    else:
        global errorSemantic
        errorSemantic = 1
        print("Semantic error. Trying to assign different type to INT variable.", p[2])

def p_statement_variable_expression(p):
    '''statement : INT ID EQUAL simple_expression  SEMICOLON'''

    # Check if the expression is of type int
    if (isinstance(p[4], int)):
        # Declare the variable with type "int"
        if declare_variable(p[2], "int", p[4]):
            # Store the variable information in the parse tree node
            #print('New variable', "int", p[2], p[3], p[4], p[5])
            p[0] = p[4]
            postfix.append(p[2])
            postfix.append("S")
        
    else:
        errorSemantic = 1
        print("Semantic error. Trying to assing different type to INT variable.", p[2])

def p_statement_variable_bool(p):
    '''statement : BOOL ID EQUAL simple_expression  SEMICOLON'''
    
     # Check if the expression is of type int
    
    if (isinstance(p[4], bool)):
        # Declare the variable with type "int"
        if declare_variable(p[2], "bool",p[4] ):
            # Store the variable information in the parse tree node
            #print('variable', "bool", p[2], p[3], p[4], p[5])
            p[0] = p[4]
            postfix.append(p[2])
            postfix.append("S")
    else:
        errorSemantic = 1
        print("Semantic error. Trying to assing different type to BOOL variable.", p[2])
     
    # Print the current symbol table for debugging
    #print(f"Tabla de simbolos :  <int id=expression>")

    #print(symbol_table)
    #print(f"-----------------")


def p_statement_assignment_number(p):
    '''statement : ID EQUAL NUMBER SEMICOLON'''
    if assign_variable(p[1], p[3]):
        p[0] = p[3]
        # Reordenar los elementos en la pila
        postfix.append(p[3])  # El valor asignado
        postfix.append(p[1])   # El nombre de la variable
        postfix.append('A')    # La operación "A"
    else:
        global errorSemantic
        errorSemantic = 1
        print("Semantic error. Incompatible Assignment")


def p_statement_assignment_expression(p):
    '''statement : ID EQUAL simple_expression SEMICOLON'''

    if assign_variable(p[1], p[3]):
        p[0]=p[3]
        postfix.append(p[1])
        postfix.append("A")
    else:
        errorSemantic = 1
        print("Semantic error. Incompatible Assignment")

#statement
#block
def p_statement_if(p):

    '''statement : IF LPAREN logical_a RPAREN LBRACE block RBRACE '''
    #print('Resultado logico del "if"', p[3])
    p[0] = p[6]
    postfix.append("END IF") #Indica el termino del if
    
def p_statement_print(p):
    '''statement : PRINT LPAREN term RPAREN SEMICOLON'''
    p[0] = p[3]
    postfix.append("PRINT")

# Grammar rules with AST construction
#------------------------------------------------------------------------------------------
# Logical OR expression -------------------------------------------------BOOLS
# Logical OR expression
def p_logical_or_binary(p):#Segun yo esto de aqui
    'logical_a : logical_a OR logical_b'
    if (check_bool_operands(p[1] ,p[3])):
        p[0] = (p[1] or p[3])
        if postfix[-3] == "C":
            postfix[-3] = "OPERATOR"
        postfix.append("or")
    else:
        errorSemantic = 1
        print("Semantic error in OR operator")


def p_logical_or_direct(p):
    'logical_a : logical_b'
    p[0] = p[1] 
# Logical AND expression

def p_logical_or_unitary(p):
    '''logical_a : TRUE
                 | FALSE
                 | ID'''
    if p[1] not in symbol_table:
        if p[1] =="true":
            p[0] = True
        else:
            p[0] = False
    else:
        p[0] = get_variable_value(p[1])
    postfix.append(p[1])
    postfix.append("C")

def p_logical_and(p):
    'logical_b : logical_b AND logical_c'

    if (check_bool_operands(p[1] ,p[3])):
        p[0] = (p[1] and p[3])
        if postfix[-3] == "C":
            postfix[-3] = "OPERATOR"
        postfix.append("and")
    else:
        errorSemantic = 1
        print("Semantic error in AND operator")

def p_logical_and_direct(p):
    'logical_b : logical_c'  # Corrected from logical_b : logical_b
    p[0] = p[1]


# ---------------------------------------------------RELACIONALES (bool == bool y int == int)
# Equality comparator (==)
def p_comparator_equality(p):
    'logical_c : logical_c EQ logical_d'
    if check_bool_operands(p[1],p[3]) or check_int_operands(p[1],p[3]):
        p[0] = (p[1] == p[3])
        postfix.append("==")

#Not Equal Comparator (!=)
def p_comparator_notequality(p):
    'logical_c : logical_c NEQ logical_d'
    if check_bool_operands(p[1],p[3]) or check_int_operands(p[1],p[3]):
        p[0] = (p[1] != p[3])
        postfix.append("!=")

def p_comparator_equality_direct(p):#Es por que no tiene nunguna operacion de comparacion
    'logical_c : logical_d'
    p[0] = p[1]
# ---------------------------------------------------RELACIONALES (sin bool)
# Relational operator <=
def p_relational_less_equal(p):
    'logical_d : logical_d LE marked_expression'

    if (check_int_operands(p[1] ,p[3])):
        p[0] = (p[1] <= p[3])
        postfix.append("<=")
    else:
        errorSemantic = 1
        print("Semantic error in <= operator")

# Relational operator >=
def p_relational_greater_equal(p):
    'logical_d : logical_d GE marked_expression'
    
    if (check_int_operands(p[1] ,p[3])):
        p[0] = (p[1] >= p[3])
        postfix.append(">=")
    else:
        errorSemantic = 1
        print("Semantic error in >= operator")

# Relational operator <
def p_relational_less(p):
    'logical_d : logical_d LT marked_expression'
    
    if (check_int_operands(p[1] ,p[3])):
        p[0] = (p[1] < p[3])
        postfix.append("<")
    else:
        errorSemantic = 1
        print("Semantic error in < operator")

# Relational operator >
def p_relational_greater(p):
    'logical_d : logical_d GT marked_expression'

    if (check_int_operands(p[1] ,p[3])):
        p[0] = (p[1] > p[3])
        postfix.append(">")
    else:
        errorSemantic = 1
        print("Semantic error in > operator")

def p_marked_expression(p):
    '''marked_expression : expression'''
    p[0] = p[1]
    postfix.append("OPERATOR")  # Solo si es una expresión compleja

# Fallback case for simple expression without relational/comparator operations
def p_relational_simple_direct(p):
    'logical_d : marked_expression'
    p[0] = p[1]

# Reglas para expresiones simples en declaraciones o asignaciones
def p_simple_expression(p):
    'simple_expression : expression'
    p[0] = p[1]

#---------------------------------------------------------------------------------
def p_expression_plus(p):
    'expression : expression PLUS term'
    if (check_int_operands(p[1] ,p[3])):
        p[0] = p[1] + p[3]
        # Identificar los operandos de suma
        op2 = postfix.pop()  # Último operando
        op1 = postfix.pop()  # Penúltimo operando
        postfix.append(op1)  # Mantener el primer operando
        postfix.append(op2)  # Mantener el segundo operando
        postfix.append('+')  # Agregar el operador
    else:
        errorSemantic = 1
        print("Semantic error in + operand")


def p_expression_minus(p):
    'expression : expression MINUS term'
    if (check_int_operands(p[1] ,p[3])):
        p[0] = p[1] - p[3]
        # Identificar los operandos de resta
        op2 = postfix.pop()  # Último operando
        op1 = postfix.pop()  # Penúltimo operando
        postfix.append(op1)  # Mantener el primer operando
        postfix.append(op2)  # Mantener el segundo operando
        postfix.append('-')  # Agregar el operador
    else:
        errorSemantic = 1
        print("Semantic error in - operand")

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'

    if (check_int_operands(p[1] ,p[3])):
        p[0] = p[1] * p[3]
        # Identificar los operandos de multiplicación
        op2 = postfix.pop()  # Último operando
        op1 = postfix.pop()  # Penúltimo operando
        postfix.append(op1)  # Mantener el primer operando
        postfix.append(op2)  # Mantener el segundo operando
        postfix.append('*')  # Agregar el operador
    else:
        errorSemantic = 1
        print("Semantic error in * operand")

def p_term_factor(p):
    'term : factor'
    if p[1] in symbol_table:
        p[0] = get_variable_value(p[1])
    else:
        p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]
    postfix.append(p[1])

def p_factor_true(p):
    'factor : TRUE'
    p[0] = True
    postfix.append(p[1])

def p_factor_false(p):
    'factor : FALSE'
    p[0] = False
    postfix.append(p[1])

#Verifica la existencia de una variable en la symbol table.
def p_factor_variable(p):
    'factor : ID'
    p[0] = p[1]
    postfix.append(p[1])


def p_empty(p):
    'empty :'
    pass


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

def parse(data):
    parser.parse(data)
    if errorSemantic == 1:
        print("Semantic error in input!")
    else:
        print("---Symbol table---")
        print(symbol_table )
        print("\n\n\n")
        print("-----Postfix Expression-------")
        print(postfix)
        print("\n\n\n")