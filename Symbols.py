class Symbols:
    symbols_dict = dict()

    def __init__(self):
        pass

    def add_symbol(self, symbol):
        if symbol in self.symbols_dict:
            self.symbols_dict[symbol] += 1
        else:
            self.symbols_dict[symbol] = 1

    def get_dict(self):
        return self.symbols_dict
