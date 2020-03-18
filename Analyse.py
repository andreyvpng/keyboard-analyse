import Settings
from Symbols import Symbols

class Analyse:
    data = Symbols()
    log_file = Settings.log_file

    def __init__(self):
        pass

    def frequency_analysis(self):
        with open(self.log_file) as f:
            line = f.readline()
            while line != '':
                line = f.readline()
                symbol = line.rstrip()
                self.data.add_symbol(symbol);

    def get_dict(self):
        return self.data.get_dict()
