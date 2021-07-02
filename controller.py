import pyautogui
from pynput import keyboard
from evaluator import Evaluator
from preferences import Preferences
import logging


class Controller:
    def __init__(self, window):
        self.hotkey_pressed = False
        self.shift_down = False
        self.highlight_hotkey_pressed = False
        self.window = window
        pyautogui.PAUSE = Preferences.key_press_pause

    def copy(self):
        pyautogui.keyDown(Preferences.super_key)
        pyautogui.keyDown('c')
        pyautogui.keyUp('c')
        pyautogui.keyUp(Preferences.super_key)
        if self.highlight_hotkey_pressed:
            pyautogui.press('right')

    @staticmethod
    def write(text):
        text = text.replace('≈', ' approx. ')
        pyautogui.typewrite(text)

    def read_clipboard(self):
        return self.window.clipboard_get()

    def on_press(self, key):
        if repr(key) == Preferences.hotkey:
            self.hotkey_pressed = True
            self.highlight_hotkey_pressed = False
        if repr(key) == "\'\\x19\'":  # ctrl+y
            self.highlight_hotkey_pressed = True
            self.hotkey_pressed = False

    def on_release(self, key):
        if repr(key) == Preferences.hotkey_special_key:
            if self.hotkey_pressed or self.highlight_hotkey_pressed:
                self.act()
                self.hotkey_pressed = False
                self.highlight_hotkey_pressed = False

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
            result = Evaluator.basic_eval(text)
        logging.info(f'result:\n{result}')
        self.write(result)
