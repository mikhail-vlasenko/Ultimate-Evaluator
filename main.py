import pyperclip
import pyautogui
import time
from pynput import keyboard
from tkinter import Tk
import ast
from simpleeval import simple_eval


class Controller:
    def __init__(self):
        self.cmd_flag = False
        self.e_flag = False
        self.f_flag = False
        self.ctrl_e_pressed = False

    def copy(self):
        pyautogui.keyDown('command')
        pyautogui.keyDown('c')
        pyautogui.keyUp('c')
        pyautogui.keyUp('command')
        print('copied')
        # pyautogui.press('right')

    def write(self, text):
        pyautogui.typewrite(text)

    def read_clipboard(self):
        return Tk().clipboard_get()

    def on_press(self, key):
        pass

    def on_release(self, key):
        if repr(key) == "\'\\x05\'":  # ctrl + e KeyCode
            self.ctrl_e_pressed = True
        try:
            if key.char == 'e':
                pass
        except AttributeError:
            if key.name == 'ctrl':
                if self.ctrl_e_pressed:
                    self.act()
                self.e_flag = False
                self.cmd_flag = False
                self.ctrl_e_pressed = False
            if key.name == 'f9':
                self.act()

    def start(self):
        # Collect events until released
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()

    def start2(self):
        with keyboard.GlobalHotKeys({'<ctrl>+e': self.handle_hotkey()}) as h:
            h.join()

    def handle_hotkey(self):
        print('hotkey')
        self.act()

    def evaluate(self, text):
        return simple_eval(text)

    def act(self):
        self.copy()
        text = self.read_clipboard()
        result = self.evaluate(text)
        print(text)
        print(f'evaluated to {result}')
        self.write(' = ' + str(result))


controller = Controller()
controller.start()
