from error import printError


Symbol_not_found = 'Symbol not found'
Symbol_not_available = 'Symbol not available'

# There is a big definition about the scope:
# In YAPL we have the Global and Local scope
# here we need to define a protocol: The scope
# must be a string with the following structure>
# 
# <Class name> - <Global>
# <Class name> - <Local> - <Method name>

class SymbolsTable:
    def __init__(self):
        self.symbols_table = []

    def AddSymbol(self, name, type, scope, context, signature=None, line=None):
        if(self.FindSymbol(name, type, scope, context)==Symbol_not_found):
            return self.symbols_table.append((name, type, scope, context, signature))
        else:
            printError(name + ' has already been declared.', line)

    def FindSymbol(self, name, type=None, scope=None, context = None):
        if(not type and not scope and not context):
            for symbol in self.symbols_table:
                if name == symbol[0]:
                    return symbol
        elif(not type and not scope):
            for symbol in self.symbols_table:
                if (
                    name == symbol[0] and
                    context == symbol[3]
                    ):
                    return symbol
        elif(not type and not context):
            for symbol in self.symbols_table:
                if (
                    name == symbol[0] and
                    scope == symbol[2]
                    ):
                    return symbol
        elif(not type):
            for symbol in self.symbols_table:
                if (
                    name == symbol[0] and
                    scope == symbol[2] and
                    context == symbol[3]
                    ):
                    return symbol
        else:
            for symbol in self.symbols_table:
                if (
                    name == symbol[0] and
                    type == symbol[1] and
                    scope == symbol[2] and
                    context == symbol[3]
                    ):
                    return symbol
        return Symbol_not_found