import sys
import os

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from antlr4.tree.Trees import Trees
from Compiled.__my__Lexer import __my__Lexer
from Compiled.__my__Parser import __my__Parser

#Error Listener when error is detected
class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print("ERROR: when parsing line %d column %d: %s\n" % \
                        (line, column, msg))
    
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
    print(Trees.toStringTree(tree, None, parser))

def main(argv):
    test_file = argv[1]
    testGrammar(test_file)

if __name__ == '__main__':
    main(sys.argv)