import ply.lex as lex
import ply.yacc as yacc

# Tokens
tokens = ['IDENTIFIER', 'LPAREN', 'RPAREN', 'SEMI', 'COMMA']

# Regular expressions for tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMI = r';'
t_COMMA = r','

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Grammar rules
def p_function_call(p):
    'function_call : IDENTIFIER LPAREN parameters RPAREN SEMI'
    p[0] = 1

def p_parameters(p):
    '''parameters : parameter
                  | parameters COMMA parameter
                  | empty'''

def p_parameter(p):
    'parameter : IDENTIFIER'

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
data = input("Enter input: ")

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
    print("Valid function call")
else:
    print("Invalid function call")
 