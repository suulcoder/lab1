# Generated from YAPL.g4 by ANTLR 4.10
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .YAPLParser import YAPLParser
else:
    from YAPLParser import YAPLParser

# This class defines a complete generic visitor for a parse tree produced by YAPLParser.

class YAPLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by YAPLParser#program.
    def visitProgram(self, ctx:YAPLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#my_class.
    def visitMy_class(self, ctx:YAPLParser.My_classContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#MethodFeature.
    def visitMethodFeature(self, ctx:YAPLParser.MethodFeatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#DeclarationFeature.
    def visitDeclarationFeature(self, ctx:YAPLParser.DeclarationFeatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#formal.
    def visitFormal(self, ctx:YAPLParser.FormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#divideExpr.
    def visitDivideExpr(self, ctx:YAPLParser.DivideExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#ifelseExpr.
    def visitIfelseExpr(self, ctx:YAPLParser.IfelseExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#intExpr.
    def visitIntExpr(self, ctx:YAPLParser.IntExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#FunctionExpr.
    def visitFunctionExpr(self, ctx:YAPLParser.FunctionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#voidExpr.
    def visitVoidExpr(self, ctx:YAPLParser.VoidExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#trueExpr.
    def visitTrueExpr(self, ctx:YAPLParser.TrueExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#MethodExpr.
    def visitMethodExpr(self, ctx:YAPLParser.MethodExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#LetExpr.
    def visitLetExpr(self, ctx:YAPLParser.LetExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#InstanceExpr.
    def visitInstanceExpr(self, ctx:YAPLParser.InstanceExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#lessThanExpr.
    def visitLessThanExpr(self, ctx:YAPLParser.LessThanExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#BracketsExpr.
    def visitBracketsExpr(self, ctx:YAPLParser.BracketsExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#parensExpr.
    def visitParensExpr(self, ctx:YAPLParser.ParensExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#minusExpr.
    def visitMinusExpr(self, ctx:YAPLParser.MinusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#DeclarationExpr.
    def visitDeclarationExpr(self, ctx:YAPLParser.DeclarationExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#timesExpr.
    def visitTimesExpr(self, ctx:YAPLParser.TimesExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#stringExpr.
    def visitStringExpr(self, ctx:YAPLParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#negateExpr.
    def visitNegateExpr(self, ctx:YAPLParser.NegateExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#notExpr.
    def visitNotExpr(self, ctx:YAPLParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#sumExpr.
    def visitSumExpr(self, ctx:YAPLParser.SumExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#whileExpr.
    def visitWhileExpr(self, ctx:YAPLParser.WhileExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#falseExpr.
    def visitFalseExpr(self, ctx:YAPLParser.FalseExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#lessThanEqualExpr.
    def visitLessThanEqualExpr(self, ctx:YAPLParser.LessThanEqualExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#idExpr.
    def visitIdExpr(self, ctx:YAPLParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#equalExpr.
    def visitEqualExpr(self, ctx:YAPLParser.EqualExprContext):
        return self.visitChildren(ctx)



del YAPLParser