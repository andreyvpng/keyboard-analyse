import settings

import matplotlib.pyplot as plt

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

class Analyse:
    data = Symbols()
    log_file = settings.log_file

    def __init__(self):
        pass

    def frequency_analysis(self):
        with open(self.log_file) as f:
            line = f.readline()
            while line != '':
                line = f.readline()
                symbol = line.rstrip()
                self.data.add_symbol(symbol);

    @staticmethod
    def __split_array(array):
        symbols=[]
        count=[]

        for item in array:
            symbols.append(item[0])
            count.append(item[1])

        return (symbols, count)

    def __convert_dict_to_list(self):
        a = []
        data = self.data.get_dict()
        for item in data:
            a.append([item, data[item]])

        def sortSecond(val):
            return val[1]
        a.sort(key=sortSecond, reverse=True)

        return a[:25]

    def do_and_save_plot(self):
        self.frequency_analysis();

        symbols, count = self.__split_array(
                self.__convert_dict_to_list())

        fig, ax = plt.subplots()

        ax.barh(symbols, count, height=0.8)
        print(len(symbols))
        plt.savefig('analyse.png' )

    def get_dict(self):
        return self.data.get_dict()
