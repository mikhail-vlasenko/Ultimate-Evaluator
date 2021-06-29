import pyautogui
from pynput import keyboard
from evaluator import Evaluator
from preferences import Preferences
import logging


class Controller:
    def __init__(self, window):
        self.hotkey_pressed = False
        self.window = window

    @staticmethod
    def copy():
        pyautogui.keyDown(Preferences.super_key)
        pyautogui.keyDown('c')
        pyautogui.keyUp('c')
        pyautogui.keyUp(Preferences.super_key)

    @staticmethod
    def write(text):
        pyautogui.typewrite(text)

    def read_clipboard(self):
        return self.window.clipboard_get()

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
        logging.info(f'initial text\n{text}')
        if Preferences.mode == 'advanced':
            result = Evaluator.advanced_eval_wrapper(text)
        elif Preferences.mode == 'wolfram':
            result = Evaluator.wolfram_eval(text)
        else:
            result = Evaluator.simple_eval(text)
        logging.info(f'result:\n{result}')
        self.write(result)
