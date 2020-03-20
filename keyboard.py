import settings

class Symbols:
    symbols_dict = dict()
    log_file = settings.log_file

    def __init__(self):
        self.frequency_analysis()

    def frequency_analysis(self):
        with open(self.log_file) as f:
            line = f.readline()
            while line != '':
                line = f.readline()
                symbol = line.rstrip()
                self.add(symbol)

    def add(self, symbol):
        if symbol in self.symbols_dict:
            self.symbols_dict[symbol] += 1
        else:
            self.symbols_dict[symbol] = 1

    def get_dict(self):
        return self.symbols_dict

class Keyboard:
    STEP = 26
    OFFSET_X = 0
    OFFSET_Y = 1
    OFFSET = [[15, 12], [32, 40], [36, 64], [50, 90], [30, 120]]

    image_path_=""
    symbols_list = []

    def __init__(self, symbols):
        self.symbols_dict = symbols
        self.merge_common_buttons()
        self.convert_dict_to_list()

    def get_scater(self):
        x, y, count = [], [], []
        for item in self.symbols_list:
            x.append(item[0])
            y.append(item[1])
            count.append(item[2])

        return (x, y, count)

    def convert_dict_to_list(self):
      dictionary = self.symbols_dict.get_dict()

      for item in dictionary:
          x, y = self.get_coordinates_of_symbols(item)
          if x == 0 and y == 0:
              continue
          self.symbols_list.append([x, y, dictionary[item]])

      def sortByCount(val):
          return val[2]

      self.symbols_list.sort(key=sortByCount, reverse=True)

    def merge_common_buttons(self):
        symbols_for_del = []
        symbols_for_add = dict()

        dictionary = self.symbols_dict.get_dict()

        for item in dictionary:
            if item in self.common_button:
                x = self.common_button[item]
                symbols_for_del.append(item)
                value = dictionary[item]
                if x in dictionary:
                    dictionary[x] += value
                else:
                    symbols_for_add[x] = value

        for item in symbols_for_del:
            del dictionary[item]

        dictionary.update(symbols_for_add)

        return dictionary

    def get_coordinates_of_symbols(self, symbol):
        for counter, row in enumerate(self.keyboard):
            if symbol in row:
                index_of_row = counter
                index_in_row = row.index(symbol)

                x = self.OFFSET[index_of_row][self.OFFSET_X] + self.STEP * index_in_row
                y = self.OFFSET[index_of_row][self.OFFSET_Y]
                return (x, y)
        return (0, 0)

class Qwerty(Keyboard):
    image_path="qwe.png"

    keyboard = [
        # 1 row
        ["grave", "1", "2", "3","4", "5", "6", "7", "8", "9", "0",
            "minus", "equal", "backspace"],
        # 2 row
        ["tab", "q", "w", "e","r", "t", "y", "u", "i", "o", "p",
            "bracketleft", "bracketright", "backslash"],
        # 3 row
        ["caps_lock", "a", "s", "d", "f", "g", "h", "j", "k", "l",
            "semicolon", "apostrophe", "return"],
        # 4 row
        ["shift_l", "z", "x", "c", "v", "b", "n", "m", "comma",
            "period", "slash"],
        # 5 row
        ["control_l", "super_l", "alt_l", "_", "_", "space"]
    ]

    common_button = {
        # 1 row
        "asciitilde": "grave",
        "exclam": "1",
        "at": "2",
        "numbersign": "3",
        "dollar": "4",
        "percent": "5",
        "asciicircum": "6",
        "ampersand": "7",
        "asterisk": "8",
        "parenleft": "9",
        "parenright": "0",
        "underscore": "minus",
        "plus": "equal",
        # 2 row
        "braceleft": "bracketleft",
        "braceright": "bracketright",
        "bar": "backslash",
        # 3 row
        "colon": "semicolon",
        "quotedbl": "apostrophe",
        # 4 row
        "less": "comma",
        "greater": "period",
        "question": "splash"
    }
