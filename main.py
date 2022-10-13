from cmath import exp
from inspect import signature
import sys

from semanticVisitor import SemanticVisitor, symbolTable
from visitor import Visitor, get_intermidiate_code

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from antlr4.tree.Trees import Trees
from Compiled.YAPLLexer import YAPLLexer
from Compiled.YAPLParser import YAPLParser
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
    lexer = YAPLLexer(input_stream)
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)
    stream = CommonTokenStream(lexer)
    
    #Parser actions
    parser = YAPLParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    
    #Run the Start Rule
    tree = parser.program()
    
    #Pretty print of parse tree
    print("\n\n\n##############################  Parse Tree  ##############################\n")
    print(Trees.toStringTree(tree, None, parser))
    
    # Semantic evaluation
    visitor = SemanticVisitor()
    visitor.visit(tree)
    
    # window = tk.Tk()
    # window.title('Tabla de Simbolos')
    # window.geometry('800x800')
    # text_area_symboltable = tk.Text(window, width=300, height=30, font=("Calibri", 15), foreground="black")
    # text_area_symboltable.grid(column=1, row=1, columnspan=10, rowspan=50)
    # text_area_symboltable.insert(tk.INSERT,{'Symbol Name:': names, 'Type:': types,  'Scope:':scopes, 'Context': contexts})
    # window.mainloop()
    
    #Intermidiate Code
    print("\n\n\n##############################  Intermidiate Code ##############################\n")
    intermidate_code_visitor = Visitor()
    intermidate_code_visitor.visit(tree)
    temporal_vars = get_intermidiate_code()
    
    
    print("\n\n\n##############################  Cleaned Final Temporal Variables ##############################\n")
    for n in temporal_vars:
        if "="  in n.code or '0x' in n.code:
            print("T" + str(n.id))
            
    #Print Table  
    names = []
    types = []
    scopes = []
    contexts = []
    signatures = []
    sizes = []
    displacement = []
    memory = []
    print("\n\n\n##############################  Symbol Table  ##############################\n")
    for symbol in symbolTable.symbols_table:
        names.append(symbol[0])
        types.append(symbol[1])
        scopes.append(symbol[2])
        contexts.append(symbol[3])
        signatures.append(symbol[4])
        sizes.append(symbol[6])
        displacement.append(symbol[7])
        memory.append(symbol[8])
    print(tabulate({'Symbol Name:': names, 'Type:': types,  'Scope:':scopes, 'Context': contexts, 'Size (bytes)' : sizes, 'Displacement (bytes)': displacement, 'Address': memory}, headers="keys", tablefmt='fancy_grid'))
    
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