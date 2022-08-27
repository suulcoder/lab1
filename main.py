from inspect import signature
import sys
from visitor import Visitor, symbolTable

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from antlr4.tree.Trees import Trees
from Compiled.__my__Lexer import __my__Lexer
from Compiled.__my__Parser import __my__Parser
from tabulate import tabulate
from main_ui import *
from error import *
#Error Listener when error is detected
class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        errorslist.append("\nSinxtax Error: %s (at line %d:%d)\n" % \
            (msg, line, column))
        print("\nSinxtax Error: %s (at line %d:%d)\n" % \
            (msg, line, column))
    
def testGrammar(test_file):
    
    #Instantiate our error listener
    error_listener = MyErrorListener()
    
    #Stream our input file
    input_stream = FileStream(test_file)
    
    #Lexer actions
    lexer = __my__Lexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)
    stream = CommonTokenStream(lexer)
    
    #Parser actions
    parser = __my__Parser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    
    #Run the Start Rule
    tree = parser.program()
    
    #Pretty print of parse tree
    print("\n\n\n##############################  Parse Tree  ##############################\n")
    print(Trees.toStringTree(tree, None, parser))
    
    # evaluator
    visitor = Visitor()
    
    try:
        visitor.visit(tree)
    except:
        pass
    
    # #Print Table
    names = []
    types = []
    scopes = []
    contexts = []
    signatures = []
    print("\n\n\n##############################  Symbol Table  ##############################\n")
    for symbol in symbolTable.symbols_table:
        names.append(symbol[0])
        types.append(symbol[1])
        scopes.append(symbol[2])
        contexts.append(symbol[3])
        signatures.append(symbol[4])
    print(tabulate({'Symbol Name:': names, 'Type:': types,  'Scope:':scopes, 'Context': contexts}, headers="keys", tablefmt='fancy_grid'))
    # window = tk.Tk()
    # window.title('Tabla de Simbolos')
    # window.geometry('800x800')
    # text_area_symboltable = tk.Text(window, width=300, height=30, font=("Calibri", 15), foreground="black")
    # text_area_symboltable.grid(column=1, row=1, columnspan=10, rowspan=50)
    # text_area_symboltable.insert(tk.INSERT,{'Symbol Name:': names, 'Type:': types,  'Scope:':scopes, 'Context': contexts})
    # window.mainloop()
def main(argv):
    test_file = argv[1]
    testGrammar(test_file)

if __name__ == '__main__':
    main(sys.argv)
    window = tk.Tk()
    window.title('Errores')
    window.geometry('800x500')
    text_area_error = tk.Text(window, width=150, height=30, font=("Calibri", 15), foreground="black")
    text_area_error.grid(column=0, row=1, columnspan=10, rowspan=50)
    if len(errorslist) > 0:
        for i in errorslist:
            text_area_error.insert(tk.INSERT,i)
    window.mainloop()