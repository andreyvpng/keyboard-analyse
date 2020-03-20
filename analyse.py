import os
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import matplotlib.image as mpimg

import settings
from keyboard import Qwerty, Dvorak, Symbols


class Analyse:
    log_file = settings.log_file

    def __init__(self):
        pass

    def do_and_save_plot(self):
        keyboard_classes = [Dvorak, Qwerty]

        for keyboard in keyboard_classes:
            x, y, count = (keyboard)().get_scater()

            fig, ax = plt.subplots()
            ax.scatter(x, y, s=count, alpha=0.5)
            fig.tight_layout()
            img = mpimg.imread((keyboard).image_path)
            imgplot = plt.imshow(img)

            image_result_path = (keyboard).image_result_path
            directory = os.path.dirname(image_result_path)
            if not os.path.exists(directory):
                os.makedirs(directory)
            plt.savefig(image_result_path)

    def get_dict(self):
        return self.data.get_dict()
