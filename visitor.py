# Generated from YAPL.g4 by ANTLR 4.10
from Compiled.YAPLVisitor import YAPLVisitor
from symbolTable import SymbolsTable, Symbol_not_found
from error import printError

current_class = ''
current_method = ''

symbolTable = SymbolsTable()
# This class defines a complete generic visitor for a parse tree produced by YAPLParser.


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
                        _, parent_type, _, _, parent_signature = parent
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
            str(class_name),       #Name
            '',                    #Type
            '',                    #Scope: Not valid
            'Class',               #Context  
            line=class_name.getPayload().line
        )
        
        # ==============================================================
        # Important to return class_name in order to check that there
        # is a Main Class
        return class_name                                       
        # ==============================================================
                                                                

    # Visit a parse tree produced by YAPLParser#MethodFeature.
    def visitMethodFeature(self, ctx):
        name = ctx.ID()
        global current_method
        current_method = str(name)
        type = ctx.TYPE()
        symbolTable.AddSymbol(
            str(name),                     #Name
            str(type),                     #Type
            current_class,                 #Scope     
            'Method',                      #Context
            ctx.formal(),                  #Signature,
            line=ctx.ID().getPayload().line
        )
        self.visitChildren(ctx)
        
        # ==============================================================
        # Important to return ('method',name,len(ctx.formal())) 
        # in order to check Main.main() structure
        return ('method',str(name),ctx.formal(), str(type))
        # ==============================================================


    # Visit a parse tree produced by YAPLParser#AtributeFeature.
    def visitAtributeFeature(self, ctx):
        name = ctx.ID()
        type = ctx.TYPE()
        symbolTable.AddSymbol(
            str(name),                     #Name
            str(type),                     #Type
            current_class + '-Global',     #Scope     
            'Atribute',                    #Context
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
            current_class + '-Local-' + current_method,      #Scope     
            'Method Parameter',                              #Context
            line=var_name.getPayload().line
        )
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#divideExpr.
    def visitDivideExpr(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YAPLParser#ifelseExpr.
    def visitIfelseExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#intExpr.
    def visitIntExpr(self, ctx):
        #return self.visitChildren(ctx)
        return {'type':'Int', 'value':ctx.getText()}


    # Visit a parse tree produced by YAPLParser#FunctionExpr.
    def visitFunctionExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#voidExpr.
    def visitVoidExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#trueExpr.
    def visitTrueExpr(self, ctx):
        #return self.visitChildren(ctx)
        return {'type':'bool', 'value':ctx.getText()}


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
                current_class + '-Local-' + current_method,                                    #Scope     
                'Let Declaration Variable' if index == 0  else 'Let Declaration parameter',    #Context
                line=ctx.ID()[0].getPayload().line
            )
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#InstanceExpr.
    def visitInstanceExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#lessThanExpr.
    def visitLessThanExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#BracketsExpr.
    def visitBracketsExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#parensExpr.
    def visitParensExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#minusExpr.
    def visitMinusExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#DeclarationExpr.
    def visitDeclarationExpr(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YAPLParser#timesExpr.
    def visitTimesExpr(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YAPLParser#stringExpr.
    def visitStringExpr(self, ctx):
        #return self.visitChildren(ctx)
        return {'type':'String', 'value':ctx.getText()}


    # Visit a parse tree produced by YAPLParser#negateExpr.
    def visitNegateExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#notExpr.
    def visitNotExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#sumExpr.
    def visitSumExpr(self, ctx):
        return self.visitChildren(ctx)
        
    # Visit a parse tree produced by YAPLParser#whileExpr.
    def visitWhileExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#falseExpr.
    def visitFalseExpr(self, ctx):
        #return self.visitChildren(ctx)
        return {'type':'bool', 'value':ctx.getText()}


    # Visit a parse tree produced by YAPLParser#lessThanEqualExpr.
    def visitLessThanEqualExpr(self, ctx):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by YAPLParser#idExpr.
    def visitIdExpr(self, ctx):
        #return self.visitChildren(ctx)
        return {'type':'ID', 'value':ctx.getText()}


    # Visit a parse tree produced by YAPLParser#equalExpr.
    def visitEqualExpr(self, ctx):
        return self.visitChildren(ctx)