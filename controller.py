import pyautogui
from pynput import keyboard
from tkinter import Tk
from evaluator import Evaluator
from preferences import Preferences


class Controller:
    def __init__(self):
        self.hotkey_pressed = False

    @staticmethod
    def copy():
        pyautogui.keyDown(Preferences.super_key)
        pyautogui.keyDown('c')
        pyautogui.keyUp('c')
        pyautogui.keyUp(Preferences.super_key)

    @staticmethod
    def write(text):
        pyautogui.typewrite(text)

    @staticmethod
    def read_clipboard():
        return Tk().clipboard_get()

    def on_press(self, key):
        pass

    def on_release(self, key):
        if repr(key) == Preferences.hotkey:
            self.hotkey_pressed = True
        elif repr(key) == Preferences.hotkey_special_key:
            if self.hotkey_pressed:
                self.act()
                self.hotkey_pressed = False

    def start(self):
        # Collect events until released
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()

    def act(self):
        self.copy()
        text = self.read_clipboard()
        if Preferences.mode == 'advanced':
            result = Evaluator.advanced_eval_wrapper(text)
        else:
            result = Evaluator.evaluate(text)
        self.write(result)
