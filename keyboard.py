class Keyboard:
    image_path_=""
    STEP = 26

    def __init__(self):
        pass

    def get_xy_of_symbols(self, symbol):
        for row in self.keyboard:
            if symbol in row["keys"]:
                index_in_row = row["keys"].index(symbol)
                x = row["begin_x"] + self.STEP * index_in_row
                y = row["begin_y"]

                return (x, y)
        return (0, 0)

class Qwerty(Keyboard):
    image_path="qwe.png"

    keyboard = [
        {
            "begin_x": 15,
            "begin_y": 12,
            "keys": [
                "grave", "1", "2", "3","4", "5", "6", "7",
                "8", "9", "0", "minus", "=", "equal"
            ]
        },
        {
            "begin_x": 32,
            "begin_y": 40,
            "keys": [
                "Tab", "q", "w", "e","r", "t", "y", "u",
                "i", "o", "p", "bracketleft", "bracketright", "backslash"
            ]
        },
        {
            "begin_x": 36,
            "begin_y": 64,
            "keys": [
                "Caps_Lock", "a", "s", "d", "f", "g",
                "h", "j", "k", "l", "semicolon", "apostrophe", "Return"
            ]
        },
        {
            "begin_x": 50,
            "begin_y": 90,
            "keys": [
                "Shift_L", "z", "x", "c", "v",
                "b", "n", "m", "comma", "period", "slash"
            ]
        },
        {
            "begin_x": 30,
            "begin_y": 120,
            "keys": [
                "Control_L", "Super_L", "Alt_L", "_", "_", "space"
            ]
        }
    ]
