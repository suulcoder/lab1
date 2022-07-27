# Generated from YAPL.g4 by ANTLR 4.10
from Compiled.YAPLVisitor import YAPLVisitor
from SymbolTable import SymbolsTable

symbolTable = SymbolsTable()
# This class defines a complete generic visitor for a parse tree produced by YAPLParser.

class Visitor(YAPLVisitor):

    # Visit a parse tree produced by YAPLParser#my_class.
    def visitMy_class(self, ctx):
        class_name = ctx.TYPE()[0]
        symbolTable.AddSymbol(
            str(class_name),
            'Class, ' + str(class_name), 
            'Global'
        )
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#MethodFeature.
    def visitMethodFeature(self, ctx):
        func_name = ctx.ID()
        type = ctx.TYPE()
        symbolTable.AddSymbol(
            str(func_name),
            'Feature, ' + str(type),
            'Bracket Feature'
        )
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#DeclarationFeature.
    def visitDeclarationFeature(self, ctx):
        func_name = ctx.ID()
        type = ctx.TYPE()
        symbolTable.AddSymbol(
            str(func_name),
            'Feature, ' + str(type),
            'Arrow Feature'
        )
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#formal.
    def visitFormal(self, ctx):
        var_name = ctx.ID()
        type = ctx.TYPE()
        symbolTable.AddSymbol(
            str(var_name),
            str(type),
            'Function Parameter'
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
        return {'type':'INT', 'value':ctx.getText()}


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
        return {'type':'INT', 'value':ctx.getText()}


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
            children.append(self.visit(node))
        return children


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