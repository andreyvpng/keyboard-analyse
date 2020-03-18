import os
import sys

from Keylogger import Keylogger
from Symbols import Symbols

def using():
    print("Usage: python App.py {start|analys}")
    sys.exit(2)

if len(sys.argv) < 2:
    using()

command = sys.argv[1]
if command == "start":
    Keylogger().start()
elif command == "analys":
    data = Symbols()
    data.frequency_analysis()
    print(data.dict())
else:
    using()
