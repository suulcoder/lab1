from cmath import exp
from inspect import signature
import sys

from semanticVisitor import SemanticVisitor, symbolTable
from visitor import Visitor, get_intermidiate_code, get_intermidiate_code_list

from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from antlr4.tree.Trees import Trees
from Compiled.YAPLLexer import YAPLLexer
from Compiled.YAPLParser import YAPLParser
from tabulate import tabulate
from main_ui import *
from error import *
from tkinter import messagebox

lst = []
total_rows = 0
total_columns = 0
class Table:
     
    def __init__(self,root):
         
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                 
                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial',16,'bold'))
                 
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])
                
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
    if len(errorslist) == 0:
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


    format_table = "| {:>12}|" +  " {:>10}|" + " {:>10}|" + " {:>10}|" + " {:>14}|" + " {:>24}|" + " {:>8}|"
    # print(format_table.format('Symbol Name:', 'Type:',  'Scope:', 'Context:', 'Size (bytes):', 'Displacement (bytes):', 'Address:'))
    lst.append(('Symbol Name:', 'Type:',  'Scope:', 'Context:', 'Size (bytes):', 'Displacement (bytes):', 'Address:'))
    i = 0
    for name in names:
        if names[i] == None:
            names[i] == ""
        if types[i] == None:
            types[i] = ""
        if scopes[i] == None:
            scopes[i] = ""
        if contexts[i] == None:
            contexts[i] = ""
        if sizes[i] == None:
            sizes[i] = ""
        if displacement[i] == None:
            displacement[i] = ""
        if memory[i] == None:
            memory[i] = ""
        lst.append((str(names[i]), str(types[i]), str(scopes[i]), str(contexts[i]), str(sizes[i]), str(displacement[i]), str(memory[i])))
        # print(format_table.format(str(names[i]), str(types[i]), str(scopes[i]), str(contexts[i]), str(sizes[i]), str(displacement[i]), str(memory[i])))
        i += 1
    # total_rows = len(lst)
    # total_columns = len(lst[0])
    # root = Tk()
    # t = Table(root)
    # root.mainloop()
    
        
                
def main(argv):
    test_file = argv[1]
    testGrammar(test_file)

if __name__ == '__main__':
    main(sys.argv)
    window = tk.Tk()
    window.title('Console')
    window.geometry('800x500')
    text_area_error = tk.Text(window, width=150, height=30, font=("Calibri", 15), foreground="black")
    text_area_error.grid(column=0, row=1, columnspan=10, rowspan=50)
    if len(get_intermidiate_code_list()) > 0:
        for i in get_intermidiate_code_list():
            text_area_error.insert(tk.INSERT,i+"\n")
    if len(errorslist) > 0:
        for i in errorslist:
            text_area_error.insert(tk.INSERT,i)
    else:
        messagebox.showinfo("Say Hello", "Code compiled succesfully, no errors found!")
    window.mainloop()