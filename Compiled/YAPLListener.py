# Generated from YAPL.g4 by ANTLR 4.10
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .YAPLParser import YAPLParser
else:
    from YAPLParser import YAPLParser

# This class defines a complete listener for a parse tree produced by YAPLParser.
class YAPLListener(ParseTreeListener):

    # Enter a parse tree produced by YAPLParser#program.
    def enterProgram(self, ctx:YAPLParser.ProgramContext):
        pass

    # Exit a parse tree produced by YAPLParser#program.
    def exitProgram(self, ctx:YAPLParser.ProgramContext):
        pass


    # Enter a parse tree produced by YAPLParser#my_class.
    def enterMy_class(self, ctx:YAPLParser.My_classContext):
        pass

    # Exit a parse tree produced by YAPLParser#my_class.
    def exitMy_class(self, ctx:YAPLParser.My_classContext):
        pass


    # Enter a parse tree produced by YAPLParser#MethodFeature.
    def enterMethodFeature(self, ctx:YAPLParser.MethodFeatureContext):
        pass

    # Exit a parse tree produced by YAPLParser#MethodFeature.
    def exitMethodFeature(self, ctx:YAPLParser.MethodFeatureContext):
        pass


    # Enter a parse tree produced by YAPLParser#AtributeFeature.
    def enterAtributeFeature(self, ctx:YAPLParser.AtributeFeatureContext):
        pass

    # Exit a parse tree produced by YAPLParser#AtributeFeature.
    def exitAtributeFeature(self, ctx:YAPLParser.AtributeFeatureContext):
        pass


    # Enter a parse tree produced by YAPLParser#formal.
    def enterFormal(self, ctx:YAPLParser.FormalContext):
        pass

    # Exit a parse tree produced by YAPLParser#formal.
    def exitFormal(self, ctx:YAPLParser.FormalContext):
        pass


    # Enter a parse tree produced by YAPLParser#divideExpr.
    def enterDivideExpr(self, ctx:YAPLParser.DivideExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#divideExpr.
    def exitDivideExpr(self, ctx:YAPLParser.DivideExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#ifelseExpr.
    def enterIfelseExpr(self, ctx:YAPLParser.IfelseExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#ifelseExpr.
    def exitIfelseExpr(self, ctx:YAPLParser.IfelseExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#FunctionExpr.
    def enterFunctionExpr(self, ctx:YAPLParser.FunctionExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#FunctionExpr.
    def exitFunctionExpr(self, ctx:YAPLParser.FunctionExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#intExpr.
    def enterIntExpr(self, ctx:YAPLParser.IntExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#intExpr.
    def exitIntExpr(self, ctx:YAPLParser.IntExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#voidExpr.
    def enterVoidExpr(self, ctx:YAPLParser.VoidExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#voidExpr.
    def exitVoidExpr(self, ctx:YAPLParser.VoidExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#trueExpr.
    def enterTrueExpr(self, ctx:YAPLParser.TrueExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#trueExpr.
    def exitTrueExpr(self, ctx:YAPLParser.TrueExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#MethodExpr.
    def enterMethodExpr(self, ctx:YAPLParser.MethodExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#MethodExpr.
    def exitMethodExpr(self, ctx:YAPLParser.MethodExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#LetExpr.
    def enterLetExpr(self, ctx:YAPLParser.LetExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#LetExpr.
    def exitLetExpr(self, ctx:YAPLParser.LetExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#InstanceExpr.
    def enterInstanceExpr(self, ctx:YAPLParser.InstanceExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#InstanceExpr.
    def exitInstanceExpr(self, ctx:YAPLParser.InstanceExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#lessThanExpr.
    def enterLessThanExpr(self, ctx:YAPLParser.LessThanExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#lessThanExpr.
    def exitLessThanExpr(self, ctx:YAPLParser.LessThanExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#BracketsExpr.
    def enterBracketsExpr(self, ctx:YAPLParser.BracketsExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#BracketsExpr.
    def exitBracketsExpr(self, ctx:YAPLParser.BracketsExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#parensExpr.
    def enterParensExpr(self, ctx:YAPLParser.ParensExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#parensExpr.
    def exitParensExpr(self, ctx:YAPLParser.ParensExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#minusExpr.
    def enterMinusExpr(self, ctx:YAPLParser.MinusExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#minusExpr.
    def exitMinusExpr(self, ctx:YAPLParser.MinusExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#DeclarationExpr.
    def enterDeclarationExpr(self, ctx:YAPLParser.DeclarationExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#DeclarationExpr.
    def exitDeclarationExpr(self, ctx:YAPLParser.DeclarationExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#timesExpr.
    def enterTimesExpr(self, ctx:YAPLParser.TimesExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#timesExpr.
    def exitTimesExpr(self, ctx:YAPLParser.TimesExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#stringExpr.
    def enterStringExpr(self, ctx:YAPLParser.StringExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#stringExpr.
    def exitStringExpr(self, ctx:YAPLParser.StringExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#unaryExpr.
    def enterUnaryExpr(self, ctx:YAPLParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#unaryExpr.
    def exitUnaryExpr(self, ctx:YAPLParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#notExpr.
    def enterNotExpr(self, ctx:YAPLParser.NotExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#notExpr.
    def exitNotExpr(self, ctx:YAPLParser.NotExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#sumExpr.
    def enterSumExpr(self, ctx:YAPLParser.SumExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#sumExpr.
    def exitSumExpr(self, ctx:YAPLParser.SumExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#whileExpr.
    def enterWhileExpr(self, ctx:YAPLParser.WhileExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#whileExpr.
    def exitWhileExpr(self, ctx:YAPLParser.WhileExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#falseExpr.
    def enterFalseExpr(self, ctx:YAPLParser.FalseExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#falseExpr.
    def exitFalseExpr(self, ctx:YAPLParser.FalseExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#lessThanEqualExpr.
    def enterLessThanEqualExpr(self, ctx:YAPLParser.LessThanEqualExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#lessThanEqualExpr.
    def exitLessThanEqualExpr(self, ctx:YAPLParser.LessThanEqualExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#idExpr.
    def enterIdExpr(self, ctx:YAPLParser.IdExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#idExpr.
    def exitIdExpr(self, ctx:YAPLParser.IdExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#equalExpr.
    def enterEqualExpr(self, ctx:YAPLParser.EqualExprContext):
        pass

    # Exit a parse tree produced by YAPLParser#equalExpr.
    def exitEqualExpr(self, ctx:YAPLParser.EqualExprContext):
        pass


    # Enter a parse tree produced by YAPLParser#call.
    def enterCall(self, ctx:YAPLParser.CallContext):
        pass

    # Exit a parse tree produced by YAPLParser#call.
    def exitCall(self, ctx:YAPLParser.CallContext):
        pass



del YAPLParser