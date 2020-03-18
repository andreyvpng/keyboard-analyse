import Settings

class Symbols:
    symbols_dict = dict()
    log_file_path = ""

    def __init__(self):
        self.log_file_path = Settings.log_file

    def frequency_analysis(self):
        with open(self.log_file_path) as f:
            line = f.readline()
            while line != '':
                line = f.readline()
                symbol = line.rstrip()
                self.__add_symbol(symbol);

    def __add_symbol(self, symbol):
        if symbol in self.symbols_dict:
            self.symbols_dict[symbol] += 1
        else:
            self.symbols_dict[symbol] = 1

    def dict(self):
        return self.symbols_dict
