import os
import sys

from Keylogger import Keylogger
from Analyse import Analyse

def using():
    print("Usage: python App.py {start|analys}\n")
    print("start - start keylogger, all symbols will write in file(~/pylogger.log or $pylogger_file)")
    print("analys - start analyse ~/pylogger and do plot and save it in ./analyse.png")
    sys.exit(2)

if len(sys.argv) < 2:
    using()

command = sys.argv[1]
if command == "start":
    Keylogger().start()
elif command == "analyse":
    analyse = Analyse()
    analyse.do_and_save_plot()
else:
    using()
