class SymbolsTable:
    def __init__(self):
        self.symbols_table = []

    def AddSymbol(self, name, type, scope):
        if(self.FindSymbol(name)=='Symbol not found'):
            return self.symbols_table.append((name, type, scope))

    def FindSymbol(self, name):
        for symbol in self.symbols_table:
            if name == symbol[0]:
                return symbol
        return 'Symbol not found'