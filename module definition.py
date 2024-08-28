import ply.lex as lex
import ply.yacc as yacc

# Keywords in the language
reserved = {'class': 'CLASS', 'public': 'PUBLIC', 'private': 'PRIVATE', 'protected': 'PROTECTED', 'void': 'VOID', 'static':'STATIC', 'int':'INT'}

# Tokens
tokens = ['LBRACE', 'RBRACE', 'IDENTIFIER', 'LPAREN', 'RPAREN', 'COMMA'] + list(reserved.values())

t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_ignore = ' \t\n'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Grammar rules of the language
def p_function_definition(p):
    'function_definition : access_specifier return_type IDENTIFIER LPAREN parameter_list RPAREN LBRACE RBRACE'
    p[0] = 1

def p_access_specifier(p):
    '''access_specifier : PUBLIC
                        | PRIVATE
                        | STATIC
                        | PROTECTED
                        | empty'''

def p_return_type(p):
    '''return_type : VOID
                   | INT
                   | IDENTIFIER'''

def p_parameter_list(p):
    '''parameter_list : parameter
                     | parameter_list COMMA parameter
                     | empty'''

def p_parameter(p):
    '''parameter : type IDENTIFIER'''

def p_type(p):
    '''type : INT
            | IDENTIFIER'''

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

data = input("Enter input: ")
# Input data to lexer
lexer.input(data)
# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break

    # print(tok)

result = parser.parse(data)
if result:
    print("Valid function definition")
else:
    print("Invalid function definition")
