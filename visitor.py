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

def addLineToIntermidiateCode(line):
    file = open('./intermediate_code.txt', 'a')
    file.write(line)
    file.truncate()
    
    
class YAPLVisitor(YAPLVisitor):
    
    # Visit a parse tree produced by YAPLParser#program.
    def visitProgram(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#my_class.
    def visitMy_class(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#MethodFeature.
    def visitMethodFeature(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#AtributeFeature.
    def visitAtributeFeature(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#formal.
    def visitFormal(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#divideExpr.
    def visitDivideExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#inStringExpr.
    def visitInStringExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#voidExpr.
    def visitVoidExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#trueExpr.
    def visitTrueExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#InstanceExpr.
    def visitInstanceExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#BracketsExpr.
    def visitBracketsExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#minusExpr.
    def visitMinusExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#stringExpr.
    def visitStringExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#outIntExpr.
    def visitOutIntExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#unaryExpr.
    def visitUnaryExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#sumExpr.
    def visitSumExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#falseExpr.
    def visitFalseExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#inBoolExpr.
    def visitInBoolExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#ifelseExpr.
    def visitIfelseExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#FunctionExpr.
    def visitFunctionExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#intExpr.
    def visitIntExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#LetExpr.
    def visitLetExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#lessThanExpr.
    def visitLessThanExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#parensExpr.
    def visitParensExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#inIntExpr.
    def visitInIntExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#DeclarationExpr.
    def visitDeclarationExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#timesExpr.
    def visitTimesExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#notExpr.
    def visitNotExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#whileExpr.
    def visitWhileExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#outBoolExpr.
    def visitOutBoolExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#outStringExpr.
    def visitOutStringExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#lessThanEqualExpr.
    def visitLessThanEqualExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#idExpr.
    def visitIdExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#equalExpr.
    def visitEqualExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#call.
    def visitCall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#parameter.
    def visitParameter(self, ctx):
        return self.visitChildren(ctx)


