from controller import Controller
from gui import GuiWindow
import logging
import threading
from preferences import Preferences


if __name__ == '__main__':
    logging.basicConfig(filename='evaluator.log', level=logging.DEBUG)
    Preferences.read('prefs.txt')
    window = GuiWindow()
    controller = Controller(window)
    cont_thread = threading.Thread(target=controller.start)
    cont_thread.start()
    window.mainloop()
