import os
import sys

from Keylogger import Keylogger
from Analyse import Analyse

def using():
    print("Usage: python App.py {start|analys}")
    sys.exit(2)

if len(sys.argv) < 2:
    using()

command = sys.argv[1]
if command == "start":
    Keylogger().start()
elif command == "analys":
    analyse = Analyse()
    analyse.do_and_save_plot()
    print(analyse.get_dict())
else:
    using()
