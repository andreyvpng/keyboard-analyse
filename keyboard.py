class Keyboard:
    image_path_=""

    STEP = 26
    OFFSET_X = 0
    OFFSET_Y = 1
    OFFSET = [
        [15, 12],
        [32, 40],
        [36, 64],
        [50, 90],
        [30, 120]]

    def __init__(self):
        pass

    def merge_common_buttons(self, dictionary):
        symbols_for_del = []
        symbols_for_add = dict()
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

    def get_xy_of_symbols(self, symbol):
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
