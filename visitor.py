# Generated from YAPL.g4 by ANTLR 4.10
from Compiled.YAPLVisitor import YAPLVisitor
from symbolTable import SymbolsTable, Symbol_not_found
from expresion import Expresion
from error import printError

current_class = ''
current_method = ''
basic_types = ['Int','String','Bool']

symbolTable = SymbolsTable()
# This class defines a complete generic visitor for a parse tree produced by YAPLParser.

def areSameType(type1, type2, checkBoth=True):
    if(str(type1) in basic_types or str(type2) in basic_types + ['Error']):
        return str(type1) == str(type2)
    types1 = symbolTable.GetTypeInheritance(type1)
    types2 = symbolTable.GetTypeInheritance(type2)
    if(checkBoth):
        if(type1 in types2 or type2 in types1):
            return True
        return False
    else:
        if(type1 in types2):
            return True
        return False
        

class Visitor(YAPLVisitor):
    
    # Visit a parse tree produced by YAPLParser#program.
    def visitProgram(self, ctx):
        
        # Every YAPL program must contain a Main class.
        # ==============================================================
        count_main_class = 0
        for node in ctx.my_class():
            child = self.visit(node)
            if(str(child)=='Main'):
                count_main_class += 1
        if(count_main_class!=1):
            printError('Every YAPL program must contain a Main class')
        # ==============================================================

    # Visit a parse tree produced by YAPLParser#my_class.
    def visitMy_class(self, ctx):
        
        class_name = ctx.TYPE()[0]
        global current_class
        current_class = str(class_name)
        
        # The Main class must contain a main method with no formal parameters.
        # The Main class cannot inherit from any other class.
        # ==============================================================
        if(str(class_name)=='Main'):
            
            # When this condition is true it is inherting from any other class:
            if(len(ctx.TYPE())==2):                                    
                printError(
                    'The Main class cannot inherit from any other class',
                    ctx.TYPE()[1].getPayload().line,
                )
            
            # Validation of a main method with no formal parameters:
            count_main_method = 0
            for node in ctx.feature():
                child = self.visit(node)
                if(child[0]=='method' and str(child[1])=='main' and len(child[2])==0):
                    count_main_method += 1
            if(count_main_method != 1):
                printError(
                    'The Main class must contain a main method with no formal parameters',
                    class_name.getPayload().line,
                )
        # ==============================================================
                    
        
        # Multiple inheritance of classes and recursive inheritance is not possible.
        # Class inheritance validation
        # If B inherits from A and B overrides a method of A, this method must have the same signature with which it was declared in A.
        # ==============================================================
        elif(len(ctx.TYPE())==2):
            
            #if father class is int string or bool: error 
            if(str(ctx.TYPE()[1]) in basic_types):
                printError(
                    'Inheritance with a basic type is not possible.',
                    ctx.TYPE()[1].getPayload().line,
                )
            
            #Recursive inheritance
            if(str(class_name) == str(ctx.TYPE()[1])):
                printError(
                    'Recursive inheritance is not possible.',
                    ctx.TYPE()[1].getPayload().line,
                )
                
            #Inheritance of not defined class
            if(
                symbolTable.FindSymbol(
                    name=str(ctx.TYPE()[1]), context='Class'
                    ) == Symbol_not_found
                ):
                printError(
                    str(ctx.TYPE()[1]) + ' not defined',
                    ctx.TYPE()[1].getPayload().line,
                )
            for node in ctx.feature():
                child = self.visit(node)
                
                #Checking method signatures
                if(child[0]=='method'):
                    method_name = child[1]
                    method_type = child[3]
                    method_signature = child[2]
                    parent_name = str(ctx.TYPE()[1])
                    
                    #Find if method is being overwritten
                    parent = symbolTable.FindSymbol(
                        method_name,
                        scope=parent_name,
                        context='Method'
                    )
                    
                    if parent!=Symbol_not_found:
                        _, parent_type, _, _, parent_signature, _ = parent
                        valid = parent_type==method_type and len(method_signature)==len(parent_signature)
                        if(valid and len(method_signature)!=0):
                            for index in range(0,len(method_signature)):
                                method_formal = method_signature[index]
                                parent_formal = parent_signature[index]
                                valid = (valid and 
                                         str(method_formal.ID())==str(parent_formal.ID()) and 
                                         str(method_formal.TYPE())==str(parent_formal.TYPE()))
                        if(not valid):
                            printError(
                                parent_name + '.' + method_name + ' is beign over overtwritten but signature does not match with ' + current_class + '.'+ method_name + ' method.'
                            )
        # ==============================================================
        
        else:
            for node in ctx.feature():
                child = self.visit(node)
        
        symbolTable.AddSymbol(
            str(class_name),                                                #Name
            ctx.TYPE()[1] if len(ctx.TYPE())==2 else '',                    #Type
            '',                                                             #Scope: Not valid
            'Class',                                                        #Context  
            line=class_name.getPayload().line
        )
        
        # ==============================================================
        # Important to return class_name in order to check that there
        # is a Main Class
        current_class = ''
        return class_name                                       
        # ==============================================================
                                                                

    # Visit a parse tree produced by YAPLParser#MethodFeature.
    def visitMethodFeature(self, ctx):
        
        global current_method
        name = ctx.ID()
        type = ctx.TYPE()
        
        current_method = str(name)
        
        parameters = []
        
        formal = ctx.formal()
        for parameter in formal:
            parameters.append(self.visit(parameter)) 

        current_method = ''    
        
        symbolTable.AddSymbol(
            str(name),                                      #Name
            str(type),                                      #Type
            current_class + '-' + current_method,           #Scope     
            'Method',                                       #Context
            parameters,                                   #Signature,
            line=ctx.ID().getPayload().line
        )
        
        current_method = str(name)
        
        expr = ctx.expr()
        expr = self.visit(expr)
        
        type = str(type)
        if(type=='SELF_TYPE'):
            type = current_class
        if(expr and expr.get('type')!=str(type)):
            printError('Method type (' + str(type) + ') should be the same as returned type (' + expr.get('type') +')', ctx.start.line)
        
        # ==============================================================
        # Important to return ('method',name,len(ctx.formal())) 
        # in order to check Main.main() structure
        current_method = ''
        return ('method',str(name),ctx.formal(), str(type))
        # ==============================================================


    # Visit a parse tree produced by YAPLParser#AtributeFeature.
    def visitAtributeFeature(self, ctx):
        name = ctx.ID()
        type = ctx.TYPE()
        symbolTable.AddSymbol(
            str(name),                                      #Name
            str(type),                                      #Type
            current_class + '-' + current_method,           #Scope     
            'Atribute',                                     #Context
            line=name.getPayload().line
        )
        self.visitChildren(ctx)
        
        # ==============================================================
        # Important to return ('method',name,len(ctx.formal())) 
        # in order to check Main.main() structure
        return ('atribute',name)
        # ==============================================================


    # Visit a parse tree produced by YAPLParser#formal.
    def visitFormal(self, ctx):
        var_name = ctx.ID()
        type = ctx.TYPE()
        symbolTable.AddSymbol(
            str(var_name),                                   #Name
            str(type),                                       #Type
            current_class + '-' + current_method,            #Scope     
            'Method Parameter',                              #Context
            line=var_name.getPayload().line
        )
        self.visitChildren(ctx)
        return {'type' : str(type)}

    # Visit a parse tree produced by YAPLParser#FunctionExpr.
    def visitFunctionExpr(self, ctx):
        name = ctx.call()
        type = 'Error'
        signature = self.visit(name)
        type = signature.get('type')
        if(type=='SELF_TYPE'):
            type = signature.get('symbol')[2].split('-')[0]
        
        index = 0
        for parameter in [self.visit(parameter) for parameter in ctx.parameter()]:
            if(parameter.get('type')!= signature.get('symbol')[4][index].get('type')):
                printError("Method signature does not match", ctx.start.line)
            index += 1
            
        return {'type': type}
    
    # Visit a parse tree produced by YAPLParser#MethodExpr.
    def visitMethodExpr(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YAPLParser#LetExpr.
    def visitLetExpr(self, ctx):
        ids = ctx.ID()
        types = ctx.TYPE()
        for index in range(0, len(ids)):
            symbolTable.AddSymbol(
                str(ids[index]),                                                               #Name
                str(types[index]),                                                             #Type
                current_class + '-' +current_method,                                    #Scope     
                'Let Declaration Variable' if index == 0  else 'Let Declaration parameter',    #Context
                line=ctx.ID()[0].getPayload().line
            )
        expressions = ctx.expr()
        expressions_count = len(expressions)
        for expression in expressions:
            expressions_count -= 1
            expr = self.visit(expression)
            if(expressions_count==0):
                return expr
        return {'type': 'Object'}
        

    # Visit a parse tree produced by YAPLParser#BracketsExpr.
    def visitBracketsExpr(self, ctx):
        expressions = ctx.expr()
        expressions_count = len(expressions)
        for expression in expressions:
            expressions_count -= 1
            expr = self.visit(expression)
            if(expressions_count==0):
                return expr
        return {'type': 'Object'}

    # Visit a parse tree produced by YAPLParser#DeclarationExpr.
    def visitDeclarationExpr(self, ctx):
        ids = ctx.call()
        right = None
        left = self.visit(ids[0])
        if(len(ids)==2):
            right = self.visit(ids[1])
        else:     
            right = self.visit(ctx.expr())
        if (not areSameType(left.get('type'), right.get('type'), checkBoth=False)):
            if(left.get('type')=='Int' and right.get('type')=='Bool'):
                return {'type': 'Int'}
            elif(left.get('type')=='Bool' and right.get('type')=='Int'):
                return {'type': 'Bool'}
            else:
                printError('Static type of expression should be the same or an inherited type' , ctx.start.line)
                return {'type': 'Error'}
        return {'type': right.get('type')}
        
    # Visit a parse tree produced by YAPLParser#whileExpr.
    def visitWhileExpr(self, ctx):
        node1, node2 = ctx.expr()
        conditional = self.visit(node1)
        block = self.visit(node2)
        
        if(conditional.get('type') != 'Bool' and conditional.get('type') != 'Int'):
            printError("Control structure data type should be a Bool not " + conditional.get('type'))
            return {'type': 'Error'}
            
        return {'type': 'Object'}
    
    # Visit a parse tree produced by YAPLParser#ifelseExpr.
    def visitIfelseExpr(self, ctx):
        node1, node2, node3 = ctx.expr()
        conditional = self.visit(node1)
        
        block1 = self.visit(node2)
        block2 = self.visit(node3)
        
        if(conditional.get('type') != 'Bool' and conditional.get('type') != 'Int'):
            printError("Control structure data type should be a Bool not " + conditional.get('type'), ctx.start.line)
            return {'type': 'Error'}
        
        if(block1==None or block2 == None):
            return {'type': 'Error'}
            
        return {'type': block1.get('type')}
    
    
    # Visit a parse tree produced by YAPLParser#voidExpr.
    def visitVoidExpr(self, ctx):
        return {'type': 'Bool'}

    # Visit a parse tree produced by YAPLParser#lessThanEqualExpr.
    def visitLessThanEqualExpr(self, ctx):
        node1, node2 = ctx.expr()
        child1 = self.visit(node1)
        child2 = self.visit(node2)
            
        #Impicit cast from Int to Bool
        if(child1.get('type')=='Int'):
            child1['type'] = 'Bool'
            
        #Impicit cast from Int to Bool
        if(child2.get('type')=='Int'):
            child2['type'] = 'Bool'
        
        if (not areSameType(child1.get('type'),child2.get('type'))):
            printError('Cannot use operant "<=" between ' + child1.get('type') + ' and ' + child2.get('type'), ctx.start.line)
            return {'type': 'Error'}
        return {'type':'Bool'}
    
    # Visit a parse tree produced by YAPLParser#lessThanExpr.
    def visitLessThanExpr(self, ctx):
        node1, node2 = ctx.expr()
        child1 = self.visit(node1)
        child2 = self.visit(node2)
        
        initial1 = child1.get('type')
        initial2 = child2.get('type')
            
        #Impicit cast from Int to Bool
        if(child1.get('type')=='Int'):
            child1['type'] = 'Bool'
            
        #Impicit cast from Int to Bool
        if(child2.get('type')=='Int'):
            child2['type'] = 'Bool'
        
        if (not areSameType(child1.get('type'),child2.get('type'))):
            printError('Cannot use operant "<" between ' + initial1 + ' and ' + initial2, ctx.start.line)
            return {'type': 'Error'}
        return {'type':'Bool'}
    
    # Visit a parse tree produced by YAPLParser#equalExpr.
    def visitEqualExpr(self, ctx):
        node1, node2 = ctx.expr()
        child1 = self.visit(node1)
        child2 = self.visit(node2)
            
        #Impicit cast from Int to Bool
        if(child1.get('type')=='Int'):
            child1['type'] = 'Bool'
            
        #Impicit cast from Int to Bool
        if(child2.get('type')=='Int'):
            child2['type'] = 'Bool'
        
        if (not areSameType(child1.get('type'),child2.get('type'))):
            printError('Cannot use operant "=" between ' + child1.get('type') + ' and ' + child2.get('type'), ctx.start.line)
            return {'type': 'Error'}
        return {'type':'Bool'}
    
    # Visit a parse tree produced by YAPLParser#parensExpr.
    def visitParensExpr(self, ctx):
        expr = ctx.expr()
        child = self.visit(expr)
        return {'type':child.get('type')}
    
    # Visit a parse tree produced by YAPLParser#notExpr.
    def visitNotExpr(self, ctx):
        expr = ctx.expr()
        child = self.visit(expr)
        #Impicit cast from Int to Bool
        if(child.get('type')=='Int'):
            return {'type':'Bool'}
                
        if(child.get('type')=='Bool'):
            return {'type':'Bool'}

        printError("Not expression cannot be aplied on a " + child.get('type'), ctx.start.line)
        return {'type': 'Error'}
    
    # Visit a parse tree produced by YAPLParser#unaryExpr.
    def visitUnaryExpr(self, ctx):
        expr = ctx.expr()
        child = self.visit(expr)
        #Impicit cast from bool to int
        if(child.get('type')=='Bool'):
            return {'type':'Int'}
                
        if(child.get('type')=='Int'):
            return {'type':'Int'}

        printError("Unary expression cannot be aplied on a " + child.get('type'), ctx.start.line)
        return {'type': 'Error'}
    
    # Visit a parse tree produced by YAPLParser#sumExpr.
    def visitSumExpr(self, ctx):
        for node in ctx.expr():
            child = self.visit(node)
            
            #Impicit cast from bool to int
            if(child.get('type')=='Bool'):
                child['type'] = 'Int'
                    
            if(child.get('type')!='Int'):
                printError(child.get('type') + ' not valid with operant "+"',ctx.start.line)
                return {'type': 'Error'}
        return {'type':'Int'}
    
    # Visit a parse tree produced by YAPLParser#minusExpr.
    def visitMinusExpr(self, ctx):
        for node in ctx.expr():
            child = self.visit(node)
            
            #Impicit cast from bool to int
            if(child.get('type')=='Bool'):
                child['type'] = 'Int'
                    
            if(child.get('type')!='Int'):
                printError(child.get('type') + ' not valid with operant "-"',ctx.start.line)
                return {'type': 'Error'}
        return {'type':'Int'}
    
    # Visit a parse tree produced by YAPLParser#timesExpr.
    def visitTimesExpr(self, ctx):
        for node in ctx.expr():
            child = self.visit(node)
            
            #Impicit cast from bool to int
            if(child.get('type')=='Bool'):
                child['type'] = 'Int'
                    
            if(child.get('type')!='Int'):
                printError(child.get('type') + ' not valid with operant "*"',ctx.start.line)
                return {'type': 'Error'}
        return {'type':'Int'}
    
    # Visit a parse tree produced by YAPLParser#divideExpr.
    def visitDivideExpr(self, ctx):
        for node in ctx.expr():
            child = self.visit(node)
            
            #Impicit cast from bool to int
            if(child.get('type')=='Bool'):
                child['type'] = 'Int'
                    
            if(child.get('type')!='Int'):
                printError(child.get('type') + ' not valid with operant "/"',ctx.start.line)
                return {'type': 'Error'}
        return {'type':'Int'}

    # Visit a parse tree produced by YAPLParser#idExpr.
    def visitIdExpr(self, ctx):
        id = ctx.call()
        return self.visit(id)
    
    # Visit a parse tree produced by YAPLParser#InstanceExpr.
    def visitInstanceExpr(self, ctx):
        type = ctx.TYPE()
        self.visitChildren(ctx)
        return {'type':str(type)}
    
    # Visit a parse tree produced by YAPLParser#intExpr.
    def visitIntExpr(self, ctx):
        return {'type':'Int'}
    
    # Visit a parse tree produced by YAPLParser#stringExpr.
    def visitStringExpr(self, ctx):
        #return self.visitChildren(ctx)
        return {'type':'String'}
    
     # Visit a parse tree produced by YAPLParser#trueExpr.
    def visitTrueExpr(self, ctx):
        return {'type':'Bool'}
    
     # Visit a parse tree produced by YAPLParser#falseExpr.
    def visitFalseExpr(self, ctx):
        #return self.visitChildren(ctx)
        return {'type':'Bool'}
    
    # Visit a parse tree produced by YAPLParser#call.
    def visitCall(self, ctx):
        ids = ctx.ID()
        index = 0
        symbol = None
        if(len(ids)==1):
            symbol = symbolTable.FindSymbol(ctx.getText(), scope=current_class + '-' +current_method)
            if(symbol==Symbol_not_found):
                symbol = symbolTable.FindSymbol(ctx.getText(), scope=current_class + '-')
            if(ctx.getText()=='self'):
                return {'type':current_class}
            elif(symbol==Symbol_not_found):
                printError(ctx.getText() + ' has not been declared.', ctx.start.line)
                return {'type': 'Error'}
            return {'type':symbol[1], 'symbol': symbol}
        for node in ids:
            child = node.getText()
            if(index==0):
                symbol = symbolTable.FindSymbol(str(child))
                if(symbol==Symbol_not_found):
                    printError(child + ' has not been declared', ctx.start.line)
                    return {'type': 'Error'}
            else:
                symbol = symbolTable.FindSymbol(str(child), scope=symbol[1]+'-')
                if(symbol==Symbol_not_found):
                    printError(child + ' has not been declared in ' + symbol[1], ctx.start.line)
                    return {'type': 'Error'}
            index += 1
        return {'type': symbol[1], 'symbol': symbol}
    
    # Visit a parse tree produced by YAPLParser#parameter.
    def visitParameter(self, ctx):
        return self.visitChildren(ctx)