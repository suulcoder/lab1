from sympy import limit
from error import printError


Symbol_not_found = 'Symbol not found'
Symbol_not_available = 'Symbol not available'
limit_heap = 0

# There is a big definition about the scope:
# In YAPL we have the Global and Local scope
# here we need to define a protocol: The scope
# must be a string with the following structure>
# 
# <Class name> - 
# <Class name> - <Method name>


displacements = {
    "String": 8,
    "Int": 4,
    "Bool": 1
}

class SymbolsTable:
    def __init__(self):
        self.symbols_table = [
            # name, type, scope, context, signature=None, value=None
            ["Object", "", "", "", "", "", "", "", ""],
            ["IO", "", "", "", "Class", "", "", "", ""],
            ["Int", "Object", "", "var type", "", "", "", "", ""],
            ["String", "Object", "", "var type", "",  "", "", "", ""],
            ["Bool", "Object", "", "var type", "",  "", "", "", ""],
            # IO
        ]

    def AddSymbol(self, name, type, scope, context, signature=None, line=None, value=None):
        size = 0
        if(context!="Method"):
            size = displacements.get(type)
            
            
        if(self.FindSymbol(name, type, scope, context)==Symbol_not_found):
            memory = ""
            displacement = 0
            if(scope!= "" and scope[-1]=='-' and context!="Method"):
                current_object = scope.split('-')[0]
                if current_object in displacements:
                    displacement = displacements.get(current_object)
                    displacements[current_object] = displacement + size
                else:
                    displacements[current_object] = size
                    
            return self.symbols_table.append([name, type, scope, context, signature, value, size if size!=0 else "", displacement if context=='Atribute' else "", memory])
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
    
    def addAddress(self, name, scope, address):
        for symbol in self.symbols_table:
            if (name == symbol[0] and scope == symbol[2]):
                symbol[8] = address

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