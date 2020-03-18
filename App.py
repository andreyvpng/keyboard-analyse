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
    analyse.frequency_analysis()
    print(analyse.get_dict())
else:
    using()
