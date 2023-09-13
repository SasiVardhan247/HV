from sly import Parser
from lexer import CTokenLexer
from Program import Program
from Function import Function
from Ast import AST,AssignAst, NameAst, NumberAst,PrintAst,ReturnAst
from SymbolTable import SymbolTable,SymbolTableEntry

gst = SymbolTable()
lxr=CTokenLexer()
ln=lxr.lineno

class CTokenParser(Parser):
    tokens = CTokenLexer.tokens
    literals=CTokenLexer.literals

    def __init__(self):
        self.valid = True
        super().__init__()

    @_('main_func')
    def program(self,p):
        pr=Program()
        pr.addFunctionDetails(p[0].name,p[0])
        print("Accepted");
        return pr

    @_('return_type identifier "(" ")" "{" local_var_decl statements return_stmt "}"')
    def main_func(self, p):
        func = Function(p.return_type,p.identifier)
        p.statements.append(p.return_stmt)
        func.setStatementsAstList(p.statements)
        func.setLocalSymbolTable(gst)
        return func
    
    @_('INT')
    def return_type(self, p):
        return p.INT
    
    @_('assignment_stmt')
    def statements(self, p):
        ast=[]
        ast.append(p[0])
        return ast

    @_('print_stmt')
    def statements(self, p):
        ast=[]
        ast.append(p[0])
        return ast

    @_('assignment_stmt statements')
    def statements(self, p):
        p[1].append(p[0])
        return p[1]

    @_('print_stmt statements')
    def statements(self, p):
        p[1].append(p[0])
        return p[1]
    
    @_('identifier "=" identifier ";"')
    def assignment_stmt(self, p):
        return AssignAst(NameAst(gst.nameInSymbolTable(p[0])),NameAst(gst.nameInSymbolTable(p[2])),ln)
    
    @_('identifier "=" constant ";"')
    def assignment_stmt(self,p):
        return AssignAst(NameAst(gst.nameInSymbolTable(p.identifier)),NumberAst(p.constant),ln)
    
    @_('PRINT identifier ";"')
    def print_stmt(self, p):
        return PrintAst(gst.nameInSymbolTable(p.identifier))

    @_('decl local_var_decl',' ')
    def local_var_decl(self,p):
        pass

    @_('type identifier ";"')
    def decl(self,p):
        gst.addSymbol(SymbolTableEntry(p.identifier,p.type))
        # print(gst.nameInSymbolTable(p.identifier))
        return gst.nameInSymbolTable(p.identifier)
    
    @_('INT')
    def type(self, p):
        return 'int'
    
    @_('ID')
    def identifier(self, p):
        # print(p[0])
        return p.ID
    
    @_('NUMBER')
    def constant(self, p):
        return p[0]

    @_('RETURN NUMBER ";"')
    def return_stmt(self,p):
        return ReturnAst(NumberAst(p[1]))

    def error(self, p):
        self.valid = False
        if p is None:
            print("Syntax error at EOF")
        else:
            print(f"Syntax error at line {p.lineno}, position {p.index}, token=`{p.type}`")

if __name__ == '__main__':
    lexer = CTokenLexer()
    parser = CTokenParser()
    
    code = 'int main() {int a;a=30; print a; return 0;}'
    tokens = lexer.tokenize(code)
    result = parser.parse(tokens)

    result.print()
    # if parser.valid:
    #     print("The code is Valid") 
    # else:
    #     print("Code is not Valid")
