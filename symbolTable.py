from error import printError


Symbol_not_found = 'Symbol not found'
Symbol_not_available = 'Symbol not available'

# There is a big definition about the scope:
# In YAPL we have the Global and Local scope
# here we need to define a protocol: The scope
# must be a string with the following structure>
# 
# <Class name> - 
# <Class name> - <Method name>

count_global = 0
count_local = 0

class SymbolsTable:
    def __init__(self):
        self.symbols_table = [
            # name, type, scope, context, signature=None, value=None
            ("Object", "", "", "", "", "", "", "", ""),
            ("IO", "", "", "", "Class", "", "", "", ""),
            ("Int", "Object", "", "var type", "", "", "", "", ""),
            ("String", "Object", "", "var type", "", "",  "", "", ""),
            ("Bool", "Object", "", "var type", "", "",  "", "", ""),
            # IO
        ]

    def AddSymbol(self, name, type, scope, context, signature=None, line=None, value=None):
        size = 0
        bytes_values = False
        if('String'==type):
            size = 8
            bytes_values = True
        elif('Int'==type):
            size = 4
            bytes_values = True
        elif('Bool'==type):
            size = 1
            bytes_values = True
            
            
        if(self.FindSymbol(name, type, scope, context)==Symbol_not_found):
            global count_global
            global count_local
            displacement = 0
            memory = ""
            if(scope!= "" and scope[-1]!='-'):
                memory = "Stack"
                displacement = count_local
                count_local += size
            elif(scope!= "" and scope[-1]=='-'):
                memory = "Global"
                displacement = count_global*8
                count_global += 1
            return self.symbols_table.append((name, type, scope, context, signature, value, size if bytes_values else "", displacement if bytes_values else "", memory))
        else:
            printError(name + ' has already been declared in current scope.', line)
            
    def GetTypeInheritance(self, type):
        inheritance_types = []
        while (str(type)!=''):
            inheritance_types.append(str(type))
            for symbol in self.symbols_table:
                if(str(type) == symbol[0]):
                    type = symbol[1]     
        return inheritance_types

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
                    scope == symbol[2]
                    ):
                    return symbol
        return Symbol_not_found