# Generated from YAPL.g4 by ANTLR 4.10
from Compiled.YAPLVisitor import YAPLVisitor
from symbolTable import SymbolsTable

symbolTable = SymbolsTable()
# This class defines a complete generic visitor for a parse tree produced by YAPLParser.


def printError(error, line=None, start_index=None):
    if(line!=None and start_index!=None):
        print('\nSemantic Error: ' + error + ' (at line ' + str(line) + ':' + str(start_index) + ')\n')
    elif(line!=None):
        print('\nSemantic Error: ' + error + ' (at line ' + str(line) + ')\n')
    else:
        print('\nSemantic Error: ' + error + '\n')
        

class Visitor(YAPLVisitor):
    
    # Visit a parse tree produced by YAPLParser#program.
    def visitProgram(self, ctx):
        
        # Every YAPL program must contain a Main class.
        # ==============================================================
        is_there_a_main_class = False
        for node in ctx.my_class():
            child = self.visit(node)
            if(str(child)=='Main'):
                is_there_a_main_class = True
        if(not is_there_a_main_class):
            printError('Every YAPL program must contain a Main class')
        # ==============================================================

    # Visit a parse tree produced by YAPLParser#my_class.
    def visitMy_class(self, ctx):
        
        class_name = ctx.TYPE()[0]
        
        # The Main class must contain a main method with no formal parameters.
        # The Main class cannot inherit from any other class.
        # ==============================================================
        if(str(class_name)=='Main'):
            
            #When this condition is true it is inherting from any other class:
            if(len(ctx.TYPE())==2):                                    
                printError(
                    'The Main class cannot inherit from any other class',
                    ctx.TYPE()[1].getPayload().line,
                ) 
            is_there_a_valid_main_method = False
            
            #Validation of a main method with no formal parameters:
            for node in ctx.feature():
                child = self.visit(node)
                if(child[0]=='method' and str(child[1])=='main' and child[2]==0):
                    is_there_a_valid_main_method = True
            if(not is_there_a_valid_main_method):
                printError(
                    'The Main class must contain a main method with no formal parameters',
                    class_name.getPayload().line,
                )
        # ==============================================================
        
        symbolTable.AddSymbol(
            str(class_name),
            'Class, ' + str(class_name), 
            'Global'
        )
        
        # ==============================================================
        # Important to return class_name in order to check that there
        # is a Main Class
        return class_name                                       
        # ==============================================================
                                                                

    # Visit a parse tree produced by YAPLParser#MethodFeature.
    def visitMethodFeature(self, ctx):
        name = ctx.ID()
        type = ctx.TYPE()
        symbolTable.AddSymbol(
            str(name),
            'Feature, ' + str(type),
            'Method Feature'
        )
        self.visitChildren(ctx)
        
        # ==============================================================
        # Important to return ('method',name,len(ctx.formal())) 
        # in order to check Main.main() structure
        return ('method',name,len(ctx.formal()))
        # ==============================================================


    # Visit a parse tree produced by YAPLParser#AtributeFeature.
    def visitAtributeFeature(self, ctx):
        name = ctx.ID()
        type = ctx.TYPE()
        symbolTable.AddSymbol(
            str(name),
            'Feature, ' + str(type),
            'Atribute Feature'
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
            str(var_name),
            str(type),
            'Method Parameter'
        )
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#divideExpr.
    def visitDivideExpr(self, ctx):
        children = []
        for node in ctx.expr():
            child = self.visit(node)
            if child.get('type') == 'ID':
                type = symbolTable.FindSymbol(child.get('value'))[1]
                if type == 'Symbol not found':
                    children.append({'type':'ERROR', 'value':'ID doesnt exist in ' + ctx.getText()})
                else:
                    children.append({'type': type, 'value':child.get('value')})
            else:
                children.append(child)
        #print('division between ', children[0].get('type'), 'and', children[1].get('type'))
        if  children[0].get('type') == 'Int' and children[1].get('type') == 'Int':
            #print('Int is returned\n\n')
            return {'type':'Int', 'value':ctx.getText()}
        else: 
            #print('Error is returned\n\n' + ctx.getText())
            return {'type':'ERROR', 'value':ctx.getText()}


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
                str(ids[index]),
                str(types[index]),
                'Let Declaration Variable' if index == 0  else 'Let Declaration parameter'
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
        children = []
        for node in ctx.expr():
            child = self.visit(node)
            if child.get('type') == 'ID':
                type = symbolTable.FindSymbol(child.get('value'))[1]
                if type == 'Symbol not found':
                    children.append({'type':'ERROR', 'value':'ID doesnt exist in ' + ctx.getText()})
                else:
                    children.append({'type': type, 'value':child.get('value')})
            else:
                children.append(child)
        #print('substraction between ', children[0].get('type'), 'and', children[1].get('type'))
        if  children[0].get('type') == 'Int' and children[1].get('type') == 'Int':
            #print('Int is returned\n\n')
            return {'type':'Int', 'value':ctx.getText()}
        else: 
            #print('Error is returned\n\n' + ctx.getText())
            return {'type':'ERROR', 'value':ctx.getText()}


    # Visit a parse tree produced by YAPLParser#DeclarationExpr.
    def visitDeclarationExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#timesExpr.
    def visitTimesExpr(self, ctx):
        children = []
        for node in ctx.expr():
            child = self.visit(node)
            if child.get('type') == 'ID':
                type = symbolTable.FindSymbol(child.get('value'))[1]
                if type == 'Symbol not found':
                    children.append({'type':'ERROR', 'value':'ID doesnt exist in ' + ctx.getText()})
                else:
                    children.append({'type': type, 'value':child.get('value')})
            else:
                children.append(child)
        #print('multiplication between ', children[0].get('type'), 'and', children[1].get('type'))
        if  children[0].get('type') == 'Int' and children[1].get('type') == 'Int':
            #print('Int is returned\n\n')
            return {'type':'Int', 'value':ctx.getText()}
        else: 
            #print('Error is returned\n\n' + ctx.getText())
            return {'type':'ERROR', 'value':ctx.getText()}

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
        children = []
        for node in ctx.expr():
            child = self.visit(node)
            if child.get('type') == 'ID':
                type = symbolTable.FindSymbol(child.get('value'))[1]
                if type == 'Symbol not found':
                    children.append({'type':'ERROR', 'value':'ID doesnt exist in ' + ctx.getText()})
                else:
                    children.append({'type': type, 'value':child.get('value')})
            else:
                children.append(child)
        #print('sum between ', children[0].get('type'), 'and', children[1].get('type'))
        if  children[0].get('type') == 'Int' and children[1].get('type') == 'Int':
            #print('Int is returned\n\n')
            return {'type':'Int', 'value':ctx.getText()}
        #TODO
        elif children[0].get('type') == 'String' and children[1].get('type') == 'String':
            #print('String is returned\n\n')
            return {'type':'String', 'value':ctx.getText()}
        else: 
            #print('Error is returned\n\n')
            return {'type':'ERROR', 'value':ctx.getText()}
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