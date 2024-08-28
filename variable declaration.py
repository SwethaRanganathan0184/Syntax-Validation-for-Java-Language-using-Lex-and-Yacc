import ply.lex as lex
import ply.yacc as yacc

# Keywords in the language
reserved = {'int': 'INT', 'float': 'FLOAT', 'char': 'CHAR', 'boolean': 'BOOLEAN'}

# Tokens
tokens = ['IDENTIFIER', 'SEMI', 'ASSIGN', 'INT_LITERAL', 'FLOAT_LITERAL', 'CHAR_LITERAL', 'BOOLEAN_LITERAL', 'INT', 'FLOAT', 'CHAR', 'BOOLEAN'] + list(reserved.values())

# Regular expressions for tokens
t_SEMI = r';'
t_ASSIGN = r'='
t_INT_LITERAL = r'\d+'
t_FLOAT_LITERAL = r'\d+\.\d+'
t_CHAR_LITERAL = r'\'[a-zA-Z0-9]\''
t_BOOLEAN_LITERAL = r'true|false'
t_ignore = ' \t\n'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Grammar rules
def p_variable_declaration(p):
    '''
    variable_declaration : type IDENTIFIER optional_assignment SEMI
    '''

    p[0] = {'type': p[1], 'identifier': p[2]}
    if len(p) > 3:
        p[0]['value'] = p[3]

def p_optional_assignment(p):
    '''
    optional_assignment : ASSIGN expression
                       | empty
    '''

    if len(p) > 2:
        p[0] = p[2]
    else:
        p[0] = None

def p_expression(p):
    '''
    expression : INT_LITERAL
              | FLOAT_LITERAL
              | CHAR_LITERAL
              | BOOLEAN_LITERAL
    '''

    p[0] = p[1]

def p_type(p):
    '''
    type : INT
         | FLOAT
         | CHAR
         | BOOLEAN
    '''

    p[0] = p[1]

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# Example input
data = input("Enter variable declaration: ")

# Input data to lexer
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break

# Parse the input
result = parser.parse(data)
if result:
    print("Valid variable declaration")
    print("Type:", result['type'])
    print("Identifier:", result['identifier'])
    if 'value' in result:
        print("Value:", result['value'])
else:
    print("Invalid variable declaration")
