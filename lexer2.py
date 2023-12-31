from sly import Lexer

class CTokenLexer(Lexer):
    tokens = {INT, ID, PRINT, NUMBER, DOUBLE, DECIMAL}
    literals={'+','*','-','/','=','(',')',';','{','}',',', '%'}
    ignore = ' \t'
    INT = r'int'
    PRINT= r'print'
    DOUBLE= r'double'
    # RETURN= r'return'
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
    DECIMAL = r'[+-]?[0-9]+\.[0-9]+'
    NUMBER = r'\d+'
    # ignore_newline = r'\n+'
    
    def __init__(self):
        self.lineno = 0
    
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)
    
    def error(self, t):
        # print(f"Illegal character '{t.value[0]}'")
        # raise Exception(f"Illegal character '{t.value[0]}'")
        self.index += 1

# lexer=CTokenLexer()
# code='''
#     int main(){
#     double a,b,c,d;
#     b=1.5;
#     a=b+c*d;
#     print a;
# }
# '''
# tokens = lexer.tokenize(code)

# for tok in tokens:
#     print(tok.value)