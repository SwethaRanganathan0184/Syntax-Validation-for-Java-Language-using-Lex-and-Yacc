import ply.lex as lex
import ply.yacc as yacc

# Keywords in the language
reserved = {'if': 'IF', 'else': 'ELSE'}

# Tokens
tokens = ['INT', 'IDENTIFIER', 'INT_LITERAL', 'ASSIGN', 'PLUS', 'LT', 'SEMI',
          'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'MINUS', 'DIV', 'MUL', 'GT', 'FLOAT'] + list(reserved.values())

t_INT = r'int'
t_FLOAT = r'float'
t_ASSIGN = r'='
t_PLUS = r'\+'
t_LT = r'\<'
t_SEMI = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_MINUS = r'\-'
t_GT = r'\>'
t_MUL = r'\*'
t_DIV = r'\/'
t_ignore = ' \t\n'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

def t_INT_LITERAL(t):
    r'\d+'
    t.value = int(t.value)
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
def p_if_statement(p):
    'if_statement : IF LPAREN expression RPAREN LBRACE statement_list RBRACE'
    p[0] = 1

def p_statement_list(p):
    '''statement_list : statement statement_list
                      | statement'''

def p_statement(p):
    '''statement : IDENTIFIER ASSIGN expression SEMI
                 | IDENTIFIER assignment_operators SEMI
                 | type IDENTIFIER SEMI
                 | self_assignment_expression SEMI'''

def p_expression(p):
    '''expression : INT_LITERAL
                  | IDENTIFIER operator INT_LITERAL
                  | IDENTIFIER conditional_operators INT_LITERAL
                  | self_assignment_expression'''

def p_operator(p):
    '''operator : PLUS
                | MINUS
                | DIV
                | MUL'''

def p_condition(p):
    '''conditional_operators : LT
                            | GT
                            | ASSIGN ASSIGN
                            | LT ASSIGN
                            | GT ASSIGN'''

def p_self_assignment_expression(p):
    '''self_assignment_expression : IDENTIFIER inc_dec_operators
                                 | IDENTIFIER assignment_operators INT_LITERAL'''

def p_inc_dec_operator(p):
    '''inc_dec_operators : PLUS PLUS
                        | MINUS MINUS'''

def p_assignment(p):
    '''assignment_operators : PLUS ASSIGN
                           | MINUS ASSIGN
                           | DIV ASSIGN
                           | MUL ASSIGN'''

def p_type(p):
    '''type : INT
            | FLOAT'''

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
    print("Found an if statement.")
    print("Java if statement syntax is correct!")
else:
    print("No if statement construct found.")
    print("Java if statement syntax is not correct!")
