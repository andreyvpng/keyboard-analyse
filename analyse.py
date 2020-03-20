import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import matplotlib.image as mpimg

import settings
from keyboard import Qwerty, Symbols


class Analyse:
    log_file = settings.log_file

    def __init__(self):
        pass

    def do_and_save_plot(self):
        symbols = Symbols()
        x, y, count = Qwerty(symbols).get_scater()

        fig, ax = plt.subplots()
        ax.scatter(x, y, s=count, alpha=0.5)
        fig.tight_layout()
        img = mpimg.imread(Qwerty.image_path)
        imgplot = plt.imshow(img)

        plt.savefig('analyse.png')

    def get_dict(self):
        return self.data.get_dict()
