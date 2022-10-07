# Generated from YAPL.g4 by ANTLR 4.10
import symbol
from Compiled.YAPLVisitor import YAPLVisitor
import re
from semanticVisitor import symbolTable
from symbolTable import displacements

intermidiate_code = {}

def clean_intermidiate_code():
    _executables_functions = {}
    for node in executables_functions:
        _executables_functions[node] = [str(node) for  node in list(filter(lambda node: type(node) == TemporalVar, executables_functions[node]))]
    
    _executables_atributes = {}
    for node in executables_atributes:
        _executables_atributes[node] = [str(node) for  node in list(filter(lambda node: type(node) == TemporalVar, executables_atributes[node]))]
    
    return (_executables_functions, _executables_atributes)

def print_line(line):
    print(re.findall('_\(\d\)_', intermidiate_code[line]))
    print("\n" + line + " : \n" + intermidiate_code[line])

def get_intermidiate_code():
    executables_functions, executables_atributes = clean_intermidiate_code()
    
    #Code should initialize Main function and its atributes:
    
    print("\n\nAtributes of Main\n")
    for line in executables_atributes.get('Main'):
        print_line(line)
        
    #Code should start with Main.main()
    print("\n\nExucatbles at Main.main\n")
    for line in executables_functions.get('Main.main'):
        
        print_line(line)
    

class TemporalVar(object):
    counter = 0
    
    def __init__(self):
        self.id = TemporalVar.counter
        TemporalVar.counter += 1
        
        self.code = ''
        
    def setCode(self, code):
        intermidiate_code['_(' + str(self.id) + ')_'] = code
        self.code = code
    
    def __str__(self):
        return '_(' + str(self.id) + ')_'       

limit_stack = 1e9
limit_heap = 0
current_class = ''
current_method = ''
gen_bracket_counter = 0
basic_types = ['Int','String','Bool']
executables_functions = {}
executables_atributes = {}

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
        else:
            executables_functions[current_class + "." + current_method].append(expr) 
    
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
        temporal_return = TemporalVar()
        temporal_return.setCode("return " + str(expr))
        executables_functions[current_class + "." + current_method + "." + str(gen_bracket_counter)] += [temporal_return]
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
        temporal = TemporalVar()
        parameters = ctx.parameter()
        code = ""
        for parameter in parameters:
            param = self.visit(parameter)
            code += "\nparam " + str(param)
        code += "\n" + str(temporal) + " = call " + function_name + ", " + str(len(parameters))
        temporal.setCode(code)
        return temporal

    # Visit a parse tree produced by YAPLParser#parameter.
    def visitParameter(self, ctx):
        temporal = TemporalVar()
        var = self.visitChildren(ctx)
        temporal.setCode(str(temporal) + " = " + var)
        return temporal
    
    #------------------------------------------------------------
    
    # Visit a parse tree produced by YAPLParser#formal.
    def visitFormal(self, ctx):
        return self.visitChildren(ctx)
    
    #------------------------------------------------------------
    
    # Visit a parse tree produced by YAPLParser#InstanceExpr.
    def visitInstanceExpr(self, ctx):
        type = ctx.TYPE().getText()
        if(type == 'Int'):
            return 0
        elif(type == 'String'):
            return "''"
        elif(type == 'Bool'):
            return 'false'
        else:
            return "new " + type
    
    # Visit a parse tree produced by YAPLParser#voidExpr.
    def visitVoidExpr(self, ctx):
        temporal = TemporalVar()
        temporal_param = TemporalVar()
        temporal_param.setCode(str(temporal_param) + " = " + self.visit(ctx.expr()))
        temporal.setCode(temporal_param.code + "\nparam " + str(temporal_param) + "\n" + str(temporal) + " = call isvoid, 1")
        return temporal
    
    #------------------------------------------------------------

    # Visit a parse tree produced by YAPLParser#inBoolExpr.
    def visitInBoolExpr(self, ctx):
        temporal = TemporalVar()
        temporal.setCode(str(temporal) + " = call in_bool, 0")
        return temporal
    
    # Visit a parse tree produced by YAPLParser#inStringExpr.
    def visitInStringExpr(self, ctx):
        temporal = TemporalVar()
        temporal.setCode(str(temporal) + " = call in_string, 0")
        return temporal
    
    # Visit a parse tree produced by YAPLParser#inIntExpr.
    def visitInIntExpr(self, ctx):
        temporal = TemporalVar()
        temporal.setCode(str(temporal) + " = call in_int, 0")
        return temporal
    
    # Visit a parse tree produced by YAPLParser#outBoolExpr.
    def visitOutBoolExpr(self, ctx):
        temporal = TemporalVar()
        temporal_param = TemporalVar()
        if ctx.call():
            if self.visit(ctx.call()):
                temporal_param.setCode(str(temporal_param) + " = " + self.visit(ctx.call()))
        elif 'true' in ctx.getText():
            temporal_param.setCode(str(temporal_param) + " = true")
        elif 'false' in ctx.getText():
            temporal_param.setCode(str(temporal_param) + " = false")  
        temporal.setCode("\nparam " + str(temporal_param) + "\n" + str(temporal) + " = call out_bool, 1")
        return temporal

    # Visit a parse tree produced by YAPLParser#outStringExpr.
    def visitOutStringExpr(self, ctx):
        temporal = TemporalVar()
        temporal_param = TemporalVar()
        if ctx.call():
            if self.visit(ctx.call()):
                temporal_param.setCode(str(temporal_param) + " = " + self.visit(ctx.call()))
        else:
            temporal_param.setCode(str(temporal_param) + " = " + ctx.getText().split("(")[-1].split(")")[0])
        temporal.setCode("\nparam " + str(temporal_param) + "\n" + str(temporal) + " = call out_string, 1")
        return temporal
    
    # Visit a parse tree produced by YAPLParser#outIntExpr.
    def visitOutIntExpr(self, ctx):
        temporal = TemporalVar()
        temporal_param = TemporalVar()
        if ctx.call():
            if self.visit(ctx.call()):
                temporal_param.setCode(str(temporal_param) + " = " + self.visit(ctx.call()))
        else:
            temporal_param.setCode(str(temporal_param) + " = " + ctx.getText().split("(")[-1].split(")")[0])
        temporal.setCode("\nparam " + str(temporal_param) + "\n" + str(temporal) + " = call out_string, 1")
        return temporal
    
    #------------------------------------------------------------
    
    # Visit a parse tree produced by YAPLParser#LetExpr.
    def visitLetExpr(self, ctx):
        global limit_stack
        
        temporal = TemporalVar()
        id = str(ctx.ID())
        type = str(ctx.TYPE())
        address = hex(int(limit_stack - displacements.get(type)))
        limit_stack -= displacements.get(type)
        
        code = id + " : " + address
        if ctx.expr():
            expr = self.visit(ctx.expr())
            if expr:
                code += "\n" + id + " = " + str(expr)
        temporal.setCode(code)
        
        limit_stack += displacements.get(type)
        return temporal
    
    # Visit a parse tree produced by YAPLParser#AtributeFeature.
    def visitAtributeFeature(self, ctx):
        global limit_heap
        temporal = TemporalVar()
        id = str(ctx.ID())
        type = str(ctx.TYPE())
        address = hex(int(limit_heap))
        limit_heap += displacements.get(type)
        
        code = id + " : " + address
        if ctx.expr():
            expr = self.visit(ctx.expr())
            code += "\n" + id + " = " + str(expr)
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
        if (len(ids)==1):
            return ids[0]
        else:
            code = ids[0]
            base = symbolTable.FindSymbol(name=ids[0], scope=current_class + '-' +current_method)[1]
            for i in range(1, len(ids)):
                id = ids[i]
                symbol = symbolTable.FindSymbol(name=id, scope=base + "-")
                displacement = symbol[7]
                code += "[" + str(displacement) + "]" 
                base = symbol[1]
            return code
        
    # Visit a parse tree produced by YAPLParser#DeclarationExpr.
    def visitDeclarationExpr(self, ctx):
        calls = []
        for node in ctx.call():
            calls.append(self.visit(node))
        temporal = TemporalVar()
        if(len(calls)==2):
            temporal.setCode(str(calls[0]) + " = " + str(calls[1]))
        elif(len(calls)==1):
            temporal.setCode(str(calls[0]) + " = " + str(self.visit(ctx.expr())))
        return temporal

        
    #------------------------------------------------------------
    
    # Visit a parse tree produced by YAPLParser#whileExpr.
    def visitWhileExpr(self, ctx):
        expressions = []
        for node in ctx.expr():
            expressions.append(self.visit(node))
        temporal = TemporalVar()
        temporal_end = TemporalVar()
        temporal.setCode("ifFALSE " + str(expressions[0]) + " goto " + str(temporal_end) + "\n" + expressions[1].code + "\ngoto " + str(temporal))
        temporal_end.setCode('')
        return temporal
    
    #------------------------------------------------------------
    
    # Visit a parse tree produced by YAPLParser#ifelseExpr.
    def visitIfelseExpr(self, ctx):
        expressions = []
        temporal = TemporalVar()
        for node in ctx.expr():
            expressions.append(self.visit(node))
        temporal.setCode("if " + str(expressions[0]) + " goto " + str(expressions[1]) + " \ngoto " + str(expressions[2]))
        return temporal
    
    #------------------------------------------------------------
    
    # Visit a parse tree produced by YAPLParser#sumExpr.
    def visitSumExpr(self, ctx):
        expressions = []
        temporal = TemporalVar()
        for node in ctx.expr():
            expressions.append(self.visit(node))
        temporal.setCode(str(temporal) + ' = ' + str(expressions[0]) + ' + ' + str(expressions[1]))
        return temporal
    
    # Visit a parse tree produced by YAPLParser#minusExpr.
    def visitMinusExpr(self, ctx):
        expressions = []
        temporal = TemporalVar()
        for node in ctx.expr():
            expressions.append(self.visit(node))
        temporal.setCode(str(temporal) + ' = ' + str(expressions[0]) + ' - ' + str(expressions[1]))
        return temporal
    
    # Visit a parse tree produced by YAPLParser#timesExpr.
    def visitTimesExpr(self, ctx):
        expressions = []
        temporal = TemporalVar()
        for node in ctx.expr():
            expressions.append(self.visit(node))
        temporal.setCode(str(temporal) + ' = ' + str(expressions[0]) + ' * ' + str(expressions[1]))
        return temporal
    
    # Visit a parse tree produced by YAPLParser#divideExpr.
    def visitDivideExpr(self, ctx):
        expressions = []
        temporal = TemporalVar()
        for node in ctx.expr():
            expressions.append(self.visit(node))
        temporal.setCode(str(temporal) + ' = ' + str(expressions[0]) + ' / ' + str(expressions[1]))
        return temporal
    
    # Visit a parse tree produced by YAPLParser#unaryExpr.
    def visitUnaryExpr(self, ctx):
        temporal = TemporalVar()
        temporal.setCode(str(temporal) + ' = -' + str(self.visit(ctx.expr())))
        return temporal

    # Visit a parse tree produced by YAPLParser#lessThanExpr.
    def visitLessThanExpr(self, ctx):
        expressions = []
        temporal = TemporalVar()
        for node in ctx.expr():
            expressions.append(self.visit(node))
        temporal.setCode(str(temporal) + ' = ' + str(expressions[0]) + ' < ' + str(expressions[1]))
        return temporal

    # Visit a parse tree produced by YAPLParser#parensExpr.
    def visitParensExpr(self, ctx):
        temporal = TemporalVar()
        temporal.setCode(str(temporal) + ' = ' + str(self.visit(ctx.expr())))
        return temporal
    
    # Visit a parse tree produced by YAPLParser#lessThanEqualExpr.
    def visitLessThanEqualExpr(self, ctx):
        expressions = []
        temporal = TemporalVar()
        for node in ctx.expr():
            expressions.append(self.visit(node))
        temporal.setCode(str(temporal) + ' = ' + str(expressions[0]) + ' <= ' + str(expressions[1]))
        return temporal
    
    # Visit a parse tree produced by YAPLParser#equalExpr.
    def visitEqualExpr(self, ctx):
        expressions = []
        temporal = TemporalVar()
        for node in ctx.expr():
            expressions.append(self.visit(node))
        temporal.setCode(str(temporal) + ' = ' + str(expressions[0]) + ' == ' + str(expressions[1]))
        return temporal
    
    # Visit a parse tree produced by YAPLParser#notExpr.
    def visitNotExpr(self, ctx):
        temporal = TemporalVar()
        temporal.setCode(str(temporal) + ' =  NOT' + str(self.visit(ctx.expr())))
        return temporal
    
    #------------------------------------------------------------
    
    # Visit a parse tree produced by YAPLParser#stringExpr.
    def visitStringExpr(self, ctx):
        return ctx.getText()
    
    # Visit a parse tree produced by YAPLParser#intExpr.
    def visitIntExpr(self, ctx):
        return ctx.getText()
    
    # Visit a parse tree produced by YAPLParser#trueExpr.
    def visitTrueExpr(self, ctx):
        return 'true'
    
    # Visit a parse tree produced by YAPLParser#falseExpr.
    def visitFalseExpr(self, ctx):
        return 'false'

