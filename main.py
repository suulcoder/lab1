from inspect import signature
import sys
from visitor import Visitor, symbolTable

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from antlr4.tree.Trees import Trees
from Compiled.YAPLLexer import YAPLLexer
from Compiled.YAPLParser import YAPLParser
from tabulate import tabulate
#Error Listener when error is detected
class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
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
    #print(Trees.toStringTree(tree, None, parser))
    
    # evaluator
    visitor = Visitor()
    output = visitor.visit(tree)
    
    # #Print Table
    names = []
    types = []
    scopes = []
    contexts = []
    signatures = []
    values = []
    print("\n\n\n##############################  Symbol Table  ##############################\n")
    for symbol in symbolTable.symbols_table:
        names.append(symbol[0])
        types.append(symbol[1])
        scopes.append(symbol[2])
        contexts.append(symbol[3])
        signatures.append(symbol[4])
        values.append(symbol[5])
    print(tabulate({'Symbol Name:': names, 'Type:': types,  'Scope:':scopes, 'Context': contexts, 'Values': values}, headers="keys", tablefmt='fancy_grid'))

def main(argv):
    test_file = argv[1]
    testGrammar(test_file)

if __name__ == '__main__':
    main(sys.argv)