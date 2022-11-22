# Generated from YAPL.g4 by ANTLR 4.10
import symbol
from tkinter import NONE
from Compiled.YAPLVisitor import YAPLVisitor
import re
from semanticVisitor import symbolTable, Symbol_not_found
from symbolTable import displacements
intermediate_code_list = []
intermidiate_code = {}
stack_classes = []
io_methods = ['in_string','in_int','in_bool','out_string','out_int','out_string']
stack_methods = []
limit_stack = 1e9
limit_heap = 0
current_class = ''
current_method = ''
gen_bracket_counter = 0
basic_types = ['Int','String','Bool']
executables_functions = {}
executables_atributes = {}
formals_functions = {}
temporal_vars = []
intermidate_code_list = []

def get_intermidiate_code_list():
    global intermidate_code_list
    return intermediate_code_list
    
def print_intermidiate_code(my_string):
    global intermidate_code_list
    intermediate_code_list.append(my_string)
    print(my_string)

def clean_intermidiate_code():
    _executables_functions = {}
    for node in executables_functions:
        _executables_functions[node] = [str(node) for  node in list(filter(lambda node: type(node) == TemporalVar, executables_functions[node]))]
    
    _executables_atributes = {}
    for node in executables_atributes:
        _executables_atributes[node] = [str(node) for  node in list(filter(lambda node: type(node) == TemporalVar, executables_atributes[node]))]
    
    _formal_functions = {}
    for node in formals_functions:
        _formal_functions[node] = [str(node) for  node in list(filter(lambda node: type(node) == TemporalVar, formals_functions[node]))]
    
    return (_executables_functions, _executables_atributes, _formal_functions)

def bakers_mark_and_sweep_algorithm(unscanned):
    global temporal_vars
    scanned = []
    _unreached = unscanned[:]
    while (len(unscanned)!=0):
        o = unscanned.pop(0)
        scanned.append(o)
        unreached = [n.split(' ')[1] for n in re.findall('= T\d+', o.code)]
        referenced_objects = re.findall('T\d+', o.code)
        for n in _unreached:
            if "T" + str(n.id) in referenced_objects:
                if "T" + str(n.id) in unreached:
                    _unreached.remove(n)
    temporal_vars = _unreached

def print_line(line):
    
    # ==============================================================    
    # Get the generated code for the line
    code = intermidiate_code[str(line)]
    # ==============================================================
    
    if("if" in code or "while" in code):
        # ============================================================== 
        # Print line
        print_intermidiate_code("\n" + str(line) + " : \n" + intermidiate_code[str(line)])
        intermidate_code_list.append(str(line) + " :")
        intermidate_code_list.append(intermidiate_code[str(line)])
        # ============================================================== 
    # ==============================================================
    # Get the related lines to the current line
    related_lines = re.findall('_\(\d+\)_', code[:]) + ['_(' + n[1:] + ')_' for n in re.findall('T\d+', code[:])]
    for related_line in related_lines:
        if related_line != line:
            print_line(related_line)
    # ==============================================================   
    
    # ==============================================================
    # Check if there is an instance of an object
    instance = re.findall('new .*', code[:])
    if(len(instance)>0):
        #Get the name of the Object
        instance = instance[0].split('new ')[-1]
        if instance not in stack_classes:
            stack_classes.append(instance)
    # ============================================================== 
    
    # ==============================================================
    # Check if there is code of a bracket section
    instance = re.findall('execute .*', code[:])
    if(len(instance)>0):
        #Get the name of the Object
        instance = instance[0].split('execute ')[-1]
        if instance not in stack_methods:
            stack_methods.append(instance.split(",")[0])
    # ============================================================== 
    
    # ==============================================================
    # Check if there is code of a method section
    instance = re.findall('call .*,', code[:])
    if(len(instance)>0):
        #Get the name of the Object
        instance = instance[0].split('call ')[-1].split(',')[0]
        if instance not in stack_methods and instance not in io_methods:
            stack_methods.append(instance)
    # ============================================================== 
    
    if("if" not in code and "while" not in code):
        # ============================================================== 
        # Print line
        print_intermidiate_code("\n" + str(line) + " : \n" + intermidiate_code[str(line)])
        intermidate_code_list.append(str(line) + " :")
        intermidate_code_list.append(intermidiate_code[str(line)])
        # ============================================================== 
    

def get_intermidiate_code():
    executables_functions, executables_atributes, formals_functions = clean_intermidiate_code()
    
    #Code should initialize Main function and its atributes:
    
    print_intermidiate_code("\n\n++++++++++++++++  Atributes of Main  ++++++++++++++++\n")
    intermidate_code_list.append("++++++++++++++++  Atributes of Main  ++++++++++++++++")
    for line in executables_atributes.get('Main'):
        print_line(line)
        
    #Code should start with Main.main()
    print_intermidiate_code("\n\n++++++++++++++++  Exucatbles at Main.main  ++++++++++++++++\n")
    intermidate_code_list.append("++++++++++++++++  Exucatbles at Main.main  ++++++++++++++++")
    for line in executables_functions.get('Main.main'):
        print_line(line)
        
    for instance in stack_classes:
        print_intermidiate_code("\n\n++++++++++++++++  Atributes of " + instance +"  ++++++++++++++++\n")
        intermidate_code_list.append("++++++++++++++++  Atributes of " + instance +"  ++++++++++++++++")
        for line in executables_atributes.get(instance):
            print_line(line)
            
        print_intermidiate_code("\n\n++++++++++++++++  End of " + method + "  ++++++++++++++++\n")
        intermidate_code_list.append("++++++++++++++++  End of " + method + "  ++++++++++++++++")
        
            
    for method in stack_methods:
        print_intermidiate_code("\n\n++++++++++++++++  Exucatbles at " + method + "  ++++++++++++++++\n")
        intermidate_code_list.append("++++++++++++++++  Exucatbles at " + method + "  ++++++++++++++++")
        
        if method.count('.')==1:
            for parameter in formals_functions.get(method):
                print_line(parameter)
        
        for line in executables_functions.get(method):
            print_line(line)
            
        print_intermidiate_code("\n\n++++++++++++++++  End of " + method + "  ++++++++++++++++\n")
        intermidate_code_list.append("++++++++++++++++  End of " + method + "  ++++++++++++++++")
        
    
    return temporal_vars, intermidate_code_list
    

class TemporalVar(object):
    counter = 0
    
    def __init__(self, type=None):
        self.id = TemporalVar.counter
        TemporalVar.counter += 1
        self.code = ''
        self.address = None
        self.type = type
        
    def assignCode(self, code):
        is_assigation = len(re.findall('T\d+ = .', code[:]))!=0
        if(is_assigation and str(self.id) in code):
            self.type = 'String' if len(re.findall('"(.*?)"', code[:]))!=0 else self.type
            self.type = 'Int' if len(re.findall('\d+', code[:]))!=0 else self.type
            self.type = 'Bool' if len(re.findall('true|false', code[:]))!=0 else self.type
            if(self.type!=None):
                global limit_stack
                self.address = hex(int(limit_stack - displacements.get(self.type)))
                self.size = displacements.get(self.type)
                limit_stack -= displacements.get(self.type)
            self.code = code
        else:
            self.code = code
        intermidiate_code['_(' + str(self.id) + ')_'] = self.code
        
        
    def setCode(self, code):
        self.assignCode(code)
        temporal_vars.append(self)
        bakers_mark_and_sweep_algorithm(temporal_vars)
    
    def __str__(self):
        return '_(' + str(self.id) + ')_'       

def addLineToIntermidiateCode(line):
    file = open('./intermediate_code.txt', 'a')
    file.write(line)
    file.truncate()

# This class defines a complete generic visitor for a parse tree produced by YAPLParser.
    
class Visitor(YAPLVisitor):
    
    # Visit a parse tree produced by YAPLParser#program.
    def visitProgram(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YAPLParser#my_class.
    def visitMy_class(self, ctx):
        class_name = ctx.TYPE()[0]
        global current_class
        current_class = str(class_name)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YAPLParser#MethodFeature.
    def visitMethodFeature(self, ctx):
        global current_method
        name = ctx.ID()
        current_method = str(name)
        expr = self.visit(ctx.expr())
        if current_class + "." + current_method not in executables_functions:
            executables_functions[current_class + "." + current_method] = [expr]
            formals_functions[current_class + "." + current_method] = []
        else:
            executables_functions[current_class + "." + current_method].append(expr) 
        for node in ctx.formal():
            formal = self.visit(node)
            formals_functions[current_class + "." + current_method].append(formal) 
    
     #------------------------------------------------------------

    # Visit a parse tree produced by YAPLParser#BracketsExpr.
    def visitBracketsExpr(self, ctx):
        global gen_bracket_counter
        gen_bracket_counter += 1
        temporal = TemporalVar()
        expr = None
        for expression in ctx.expr():
            expr = self.visit(expression)
            if current_class + "." + current_method + "." + str(gen_bracket_counter) not in executables_functions:
                executables_functions[current_class + "." + current_method + "." + str(gen_bracket_counter)] = [expr]
            else:
                executables_functions[current_class + "." + current_method + "." + str(gen_bracket_counter)] += [expr]
        
        temporal.setCode('execute ' + current_class + "." + current_method + "." + str(gen_bracket_counter))
        gen_bracket_counter -= 1
        return temporal
            
    
    #------------------------------------------------------------

    # Visit a parse tree produced by YAPLParser#FunctionExpr.
    def visitFunctionExpr(self, ctx):
        function_name = ctx.call().getText()
        if('.' in function_name):
            ids = function_name.split('.')
            func_name = ids[-1]
            symbol = symbolTable.FindSymbol(name=ids[-2], scope=current_class + '-')
            type = symbol[1]
            function_name = type + "." + func_name
        else:
            function_name = current_class + "." + function_name
        temporal = TemporalVar()
        parameters = ctx.parameter()
        code = ""
        for parameter in parameters:
            param = self.visit(parameter)
            code += "param T" + str(param.id) + "\n"
        code += "\n" + "T" + str(temporal.id) + " = call " + function_name + ", " + str(len(parameters))
        temporal.setCode(code)
        return temporal

    # Visit a parse tree produced by YAPLParser#parameter.
    def visitParameter(self, ctx):
        temporal = TemporalVar()
        var = self.visitChildren(ctx)
        temporal.setCode("T" + str(temporal.id) + " = T" + str(var.id))
        return temporal
    
    #------------------------------------------------------------
    
    # Visit a parse tree produced by YAPLParser#formal.
    def visitFormal(self, ctx):
        temporal = TemporalVar()
        id = str(ctx.ID())
        temporal.setCode('received param ' + id)
        symbolTable.addAddress(id, current_class + '-' + current_method, '* ' + id)
        return temporal
    
    #------------------------------------------------------------
    
    # Visit a parse tree produced by YAPLParser#InstanceExpr.
    def visitInstanceExpr(self, ctx):
        type = ctx.TYPE().getText()
        temporal = TemporalVar(ctx.TYPE().getText())
        if(type == 'Int'):
            temporal.setCode("T" + str(temporal.id) + " = 0")
        elif(type == 'String'):
            temporal.setCode("T" + str(temporal.id) + " = '")
        elif(type == 'Bool'):
            temporal.setCode("T" + str(temporal.id) + " = false")
        else:
            temporal.setCode("T" + str(temporal.id) + " = new " + type)
        return temporal
    
    # Visit a parse tree produced by YAPLParser#voidExpr.
    def visitVoidExpr(self, ctx):
        temporal = TemporalVar()
        temporal_param = TemporalVar()
        temporal_param.setCode("T" + str(temporal_param.id) + " = T" + str(self.visit(ctx.expr()).id))
        temporal.setCode(temporal_param.code + "\nparam " + str(temporal_param) + "\nT" + str(temporal.id) + " = call isvoid, 1")
        return temporal
    
    #------------------------------------------------------------

    # Visit a parse tree produced by YAPLParser#inBoolExpr.
    def visitInBoolExpr(self, ctx):
        temporal = TemporalVar()
        temporal.setCode("T" + str(temporal.id) + " = call in_bool, 0")
        return temporal
    
    # Visit a parse tree produced by YAPLParser#inStringExpr.
    def visitInStringExpr(self, ctx):
        temporal = TemporalVar()
        temporal.setCode("T" + str(temporal.id) + " = call in_string, 0")
        return temporal
    
    # Visit a parse tree produced by YAPLParser#inIntExpr.
    def visitInIntExpr(self, ctx):
        temporal = TemporalVar()
        temporal.setCode("T" + str(temporal.id) + " = call in_int, 0")
        return temporal
    
    # Visit a parse tree produced by YAPLParser#outBoolExpr.
    def visitOutBoolExpr(self, ctx):
        temporal = TemporalVar()
        temporal_param = TemporalVar()
        if ctx.call():
            _call = self.visit(ctx.call())
            if _call:
                temporal_param.setCode("T" + str(temporal_param.id) + " = T" + str(_call.id))
        elif 'true' in ctx.getText():
            temporal_param.setCode("T" + str(temporal_param.id) + " = 1")
        elif 'false' in ctx.getText():
            temporal_param.setCode("T" + str(temporal_param.id) + " = 0")  
        temporal.setCode("param T" + str(temporal_param.id) + "\nT" + str(temporal.id) + " = call out_bool, 1")
        return temporal

    # Visit a parse tree produced by YAPLParser#outStringExpr.
    def visitOutStringExpr(self, ctx):
        temporal = TemporalVar()
        temporal_param = TemporalVar()
        if ctx.call():
            _call = self.visit(ctx.call())
            if _call:
                temporal_param.setCode("T" + str(temporal_param.id) + " = T" + str(_call.id))
        else:
            temporal_param.setCode("T" + str(temporal_param.id) + " = " + ctx.getText().split("(")[-1].split(")")[0])
        temporal.setCode("param T" + str(temporal_param.id) + "\nT" + str(temporal.id) + " = call out_string, 1")
        return temporal
    
    # Visit a parse tree produced by YAPLParser#outIntExpr.
    def visitOutIntExpr(self, ctx):
        temporal = TemporalVar()
        temporal_param = TemporalVar()
        if ctx.call():
            _call = self.visit(ctx.call())
            if _call:
                temporal_param.setCode("T" + str(temporal_param.id) + " = T" + str(_call.id))
        else:
            temporal_param.setCode("T" + str(temporal_param.id) + " = " + ctx.getText().split("(")[-1].split(")")[0])
        temporal.setCode("param T" + str(temporal_param.id) + "\nT" + str(temporal.id) + " = call out_int, 1")
        return temporal
    
    #------------------------------------------------------------
    
    # Visit a parse tree produced by YAPLParser#LetExpr.
    def visitLetExpr(self, ctx):
        global limit_heap
        temporal = TemporalVar()
        id = str(ctx.ID())
        type = str(ctx.TYPE())
        address = hex(int(limit_heap))
        limit_heap += displacements.get(type)
        
        code = id + " : " + address
        if ctx.expr():
            expr = self.visit(ctx.expr())
            if expr:
                code += "\n" + id + " = T" + str(expr.id)
        temporal.setCode(code)
        symbolTable.addAddress(id, current_class + "-" + current_method, address)
        return temporal
    
    # Visit a parse tree produced by YAPLParser#AtributeFeature.
    def visitAtributeFeature(self, ctx):
        code = ""
        temporal = TemporalVar()
        id = str(ctx.ID())
        type = str(ctx.TYPE())
        if(current_class == 'Main'):
            global limit_heap
            address = hex(int(limit_heap))
            limit_heap += displacements.get(type)
            code = id + " : " + address
            symbolTable.addAddress(id, current_class + "-", address)
        else:
            code = id + " : * self[" + str(symbolTable.FindSymbol(id, scope=current_class + "-")[7]) + "]"
            symbolTable.addAddress(id, current_class + "-", "* self[" + str(symbolTable.FindSymbol(id, scope=current_class + "-")[7]) + "]")
        if ctx.expr():
            expr = self.visit(ctx.expr())
            code += "\n" + id + " = T" + str(expr.id)
        temporal.setCode(code)
        
        if current_class not in executables_atributes:
            executables_atributes[current_class] = [temporal]
        else:
            executables_atributes[current_class].append(temporal) 
            
    # Visit a parse tree produced by YAPLParser#idExpr.
    def visitIdExpr(self, ctx):
        return self.visitChildren(ctx)
    
    #------------------------------------------------------------
    
    # Visit a parse tree produced by YAPLParser#call.
    def visitCall(self, ctx):
        ids = []
        for node in ctx.ID():
            ids.append(node.getText())
        symbol_ = symbolTable.FindSymbol(name=ids[0], scope=current_class + '-')
        if (len(ids)==1):
            temporal = TemporalVar()
            temporal.setCode("T" + str(temporal.id) + " = " + str(symbol_[8] if symbol_ != Symbol_not_found else ("* " + ids[0])))
            return temporal
        else:
            code = symbol_[8] if symbol_ != Symbol_not_found else ids[0]
            base = symbolTable.FindSymbol(name=ids[0], scope=current_class + '-')[1]
            for i in range(1, len(ids)):
                id = ids[i]
                symbol = symbolTable.FindSymbol(name=id, scope=base + "-")
                displacement = symbol[7]
                code += "[" + str(displacement) + "]" 
                base = symbol[1]
            temporal = TemporalVar()
            temporal.setCode("T" + str(temporal.id) + " = " + code)
            return temporal
        
    # Visit a parse tree produced by YAPLParser#DeclarationExpr.
    def visitDeclarationExpr(self, ctx):
        calls = []
        for node in ctx.call():
            calls.append(self.visit(node))
        temporal = TemporalVar()
        if(len(calls)==2):
            temporal.setCode("T" + str(calls[0].id) + " = T" + str(calls[1].id))
        elif(len(calls)==1):
            temporal.setCode("T" + str(calls[0].id) + " = T" + str(self.visit(ctx.expr()).id))
        return temporal

        
    #------------------------------------------------------------
    
    # Visit a parse tree produced by YAPLParser#whileExpr.
    def visitWhileExpr(self, ctx):
        expressions = []
        for node in ctx.expr():
            expressions.append(self.visit(node))
        temporal = TemporalVar()
        temporal.setCode("ifFALSE T" + str(expressions[0].id) + " goto " + "next" + "\n" + expressions[1].code + "\ngoto " + str(temporal))
        return temporal
    
    #------------------------------------------------------------
    
    # Visit a parse tree produced by YAPLParser#ifelseExpr.
    def visitIfelseExpr(self, ctx):
        expressions = []
        temporal = TemporalVar()
        for node in ctx.expr():
            expressions.append(self.visit(node))
        temporal.setCode("if T" + str(expressions[0].id) + " goto " + str(expressions[1]) + " \ngoto " + str(expressions[2]))
        return temporal
    
    #------------------------------------------------------------
    
    # Visit a parse tree produced by YAPLParser#sumExpr.
    def visitSumExpr(self, ctx):
        expressions = []
        temporal = TemporalVar('Int')
        for node in ctx.expr():
            expressions.append(self.visit(node))
        temporal.setCode("T" + str(temporal.id) + ' = T' + str(expressions[0].id) + ' + T' + str(expressions[1].id))
        return temporal
    
    # Visit a parse tree produced by YAPLParser#minusExpr.
    def visitMinusExpr(self, ctx):
        expressions = []
        temporal = TemporalVar('Int')
        for node in ctx.expr():
            expressions.append(self.visit(node))
        temporal.setCode("T" + str(temporal.id) + ' = T' + str(expressions[0].id) + ' - T' + str(expressions[1].id))
        return temporal
    
    # Visit a parse tree produced by YAPLParser#timesExpr.
    def visitTimesExpr(self, ctx):
        expressions = []
        temporal = TemporalVar('Int')
        for node in ctx.expr():
            expressions.append(self.visit(node))
        temporal.setCode("T" + str(temporal.id) + ' = T' + str(expressions[0].id) + ' * T' + str(expressions[1].id))
        return temporal
    
    # Visit a parse tree produced by YAPLParser#divideExpr.
    def visitDivideExpr(self, ctx):
        expressions = []
        temporal = TemporalVar('Int')
        for node in ctx.expr():
            expressions.append(self.visit(node))
        temporal.setCode("T" + str(temporal.id) + ' = T' + str(expressions[0].id) + ' / T' + str(expressions[1].id))
        return temporal
    
    # Visit a parse tree produced by YAPLParser#unaryExpr.
    def visitUnaryExpr(self, ctx):
        temporal = TemporalVar('Int')
        temporal.setCode("T" + str(temporal.id) + ' = ~ T' + str(self.visit(ctx.expr()).id))
        return temporal

    # Visit a parse tree produced by YAPLParser#lessThanExpr.
    def visitLessThanExpr(self, ctx):
        expressions = []
        temporal = TemporalVar('Bool')
        for node in ctx.expr():
            expressions.append(self.visit(node))
        temporal.setCode("T" + str(temporal.id) + ' = T' + str(expressions[0].id) + ' < T' + str(expressions[1].id))
        return temporal

    # Visit a parse tree produced by YAPLParser#parensExpr.
    def visitParensExpr(self, ctx):
        temporal = TemporalVar()
        temporal.setCode("T" + str(temporal.id) + ' = T' + str(self.visit(ctx.expr()).id))
        return temporal
    
    # Visit a parse tree produced by YAPLParser#lessThanEqualExpr.
    def visitLessThanEqualExpr(self, ctx):
        expressions = []
        temporal = TemporalVar('Bool')
        for node in ctx.expr():
            expressions.append(self.visit(node))
        temporal.setCode("T" + str(temporal.id) + ' = T' + str(expressions[0].id) + ' <= T' + str(expressions[1].id))
        return temporal
    
    # Visit a parse tree produced by YAPLParser#equalExpr.
    def visitEqualExpr(self, ctx):
        expressions = []
        temporal = TemporalVar('Bool')
        for node in ctx.expr():
            expressions.append(self.visit(node))
        temporal.setCode("T" + str(temporal.id) + ' = T' + str(expressions[0].id) + ' == T' + str(expressions[1].id))
        return temporal
    
    # Visit a parse tree produced by YAPLParser#notExpr.
    def visitNotExpr(self, ctx):
        temporal = TemporalVar('Bool')
        temporal.setCode("T" + str(temporal.id) + ' =  NOT T' + str(self.visit(ctx.expr()).id))
        return temporal
    
    #------------------------------------------------------------
    
    # Visit a parse tree produced by YAPLParser#stringExpr.
    def visitStringExpr(self, ctx):
        temporal = TemporalVar('String')
        temporal.setCode("T" + str(temporal.id) + " = " + ctx.getText())
        return temporal
    
    # Visit a parse tree produced by YAPLParser#intExpr.
    def visitIntExpr(self, ctx):
        temporal = TemporalVar('Int')
        temporal.setCode("T" + str(temporal.id) + " = " + ctx.getText())
        return temporal
    
    # Visit a parse tree produced by YAPLParser#trueExpr.
    def visitTrueExpr(self, ctx):
        temporal = TemporalVar('Bool')
        temporal.setCode("T" + str(temporal.id) + " = 1")
        return temporal
    
    # Visit a parse tree produced by YAPLParser#falseExpr.
    def visitFalseExpr(self, ctx):
        temporal = TemporalVar('Bool')
        temporal.setCode("T" + str(temporal.id) + " = 0")
        return temporal

