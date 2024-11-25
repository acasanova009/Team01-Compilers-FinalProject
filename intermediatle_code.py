from parser import parse,postfix,symbol_table,errorSemantic

indentation  = 0 #Para identacion de cada if
instructions = {'END IF', 'C' ,'S','A','>','<','>=','<=','==','!=','and','or','PRINT'} #Es un set
conditions = {'>','<','>=','<=','==','!=','and','or'}
operations = []

with open("entrada.txt", "r") as archivo:
    data = archivo.read()


def statement():
    """Procesa declaraciones de variables."""
    global indentation
    current_indent = "\t" * indentation
    var = operations.pop()  # Nombre de la variable
    #type_var = symbol_table[var]["type"]  # Tipo de la variable
    value = get_expression()  # Procesa la expresión para obtener el valor
    if value[0] == "(" and value[-1] == ")":
        value = value[1:-1]
    with open('salida.py', 'a+') as file:
        file.write(current_indent + f"{var} = {value}\n")

def assignment():
    """Procesa asignaciones de valores a variables."""
    global indentation
    current_indent = "\t" * indentation
    var = operations.pop()  # Nombre de la variable
    value = get_expression()  # Procesa la expresión para obtener el valor
    if value[0] == "(" and value[-1] == ")":
        value = value[1:-1]
    with open('salida.py', 'a+') as file:
        file.write(current_indent + f"{var} = {value}\n")


def get_expression():
    """Convierte una expresión en notación postfija a notación infija."""
    stack = []
    while operations:
        token = operations.pop(0)
        if isinstance(token, int) or token in {"True", "False"} or token in symbol_table:  # Operando
                stack.append(str(token))
        elif token in {'+', '-', '*'} or token in conditions:  # Operador
            b = stack.pop()
            a = stack.pop()
            stack.append(f"({a} {token} {b})")
        elif token == "OPERATOR":
            continue
        else:  # Si encontramos algo inesperado
            break
    return stack[0] if stack else f"({token})"

def clause_if():
    """Procesa cláusulas if."""
    global indentation
    current_indent = "\t" * indentation
    condition = get_expression()  # Condición del if
    with open('salida.py', 'a+') as file:
        file.write(current_indent + f"if {condition}: \n")
    indentation += 1  # Agrega nivel de indentación

def end_if():
    """Maneja el final de un bloque `if`."""
    global indentation
    if indentation > 0:
        indentation -= 1

def print_m():
    """Maneja las impresiones de variables, números o booleanos"""
    global indentation
    current_indent = "\t" * indentation
    element = operations.pop(0)
    with open('salida.py', 'a+') as file:
        file.write(current_indent + f"print({element})\n")

def writeFile(instruction):
    """Llama a la función adecuada según la instrucción."""
    if instruction == 'S':
        statement()
    elif instruction == 'A':
        assignment()
    elif instruction == 'C':
        clause_if()
    elif instruction in conditions:
        operations.append(instruction)
        clause_if()
    elif instruction == 'END IF':
        end_if()
    elif instruction == 'PRINT':
        print_m()

#Main
archivo = open("salida.py", "w")  # Abre el archivo en modo escritura 
archivo.close()                    # Cierra el archivo

parse(data)
if errorSemantic == 0:
 #En la notación postfija primero van los operandos y después el operador
    while len(postfix) > 0:
        operator = postfix.pop(0)
        if operator not in instructions:  # Si no es una instrucción, es una operación o valor
            operations.append(operator)
        else:
            writeFile(operator)

    print("Successful compilation!\n\n")
    with open('salida.py', 'a+') as file:
        file.seek(0)  # Mueve el puntero al inicio del archivo
        contenido = file.read()  # Lee todo el contenido
    print("-----Intermediate Code-------")
    print(contenido)
    print("-----Execution-------")
    with open("salida.py") as f:
        code = f.read()
        exec(code)  # Ejecuta el contenido del archivo