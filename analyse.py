import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import matplotlib.image as mpimg

import settings
from keyboard import Qwerty

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
        x, y, count = [], [], []
        for item in array:
            x.append(item[0])
            y.append(item[1])
            count.append(item[2])

        return (x, y, count)

    def __convert_dict_to_list(self):
        a, data = [], self.data.get_dict()

        keyboard = Qwerty()
        data = keyboard.merge_common_buttons(data)

        for item in data:
            x, y = keyboard.get_xy_of_symbols(item)
            if x == 0 and y == 0:
                continue
            a.append([x, y, data[item]])

        def sortByCount(val):
            return val[2]

        a.sort(key=sortByCount, reverse=True)
        return a

    def do_and_save_plot(self):
        self.frequency_analysis();

        x, y, count = self.__split_array(
                self.__convert_dict_to_list())

        fig, ax = plt.subplots()

        ax.scatter(x, y, s=count, alpha=0.5)

        fig.tight_layout()

        img = mpimg.imread(Qwerty.image_path)
        imgplot = plt.imshow(img)

        plt.savefig('analyse.png')

    def get_dict(self):
        return self.data.get_dict()
