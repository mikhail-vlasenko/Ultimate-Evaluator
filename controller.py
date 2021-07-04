import pyautogui
from pynput import keyboard
from evaluator import Evaluator
from preferences import Preferences
import logging
import time


class Controller:
    def __init__(self, window):
        self.hotkey_pressed = False
        self.h_hotkey_pressed = False
        self.keys_down = [False, False, False]
        self.h_keys_down = [False, False, False]
        self.window = window
        pyautogui.PAUSE = Preferences.key_press_pause

    def copy(self):
        pyautogui.keyDown(Preferences.super_key)
        pyautogui.keyDown('c')
        pyautogui.keyUp('c')
        pyautogui.keyUp(Preferences.super_key)
        if self.h_hotkey_pressed:
            pyautogui.press('right')

    @staticmethod
    def write(text):
        text = text.replace('≈', ' approx. ')
        pyautogui.typewrite(text)

    def read_clipboard(self):
        return self.window.clipboard_get()

    def on_press(self, key):
        hotkey_len = len(Preferences.hotkey)
        for i in range(hotkey_len):
            if repr(key) == Preferences.hotkey[i]:
                self.keys_down[i] = True

        if self.keys_down[0] and (hotkey_len < 2 or self.keys_down[1]) and (hotkey_len < 3 or self.keys_down[2]):
            self.hotkey_pressed = True

        hotkey_len = len(Preferences.hotkey_highlight)
        for i in range(hotkey_len):
            if repr(key) == Preferences.hotkey_highlight[i]:
                self.h_keys_down[i] = True

        if self.h_keys_down[0] and (hotkey_len < 2 or self.h_keys_down[1]) and (hotkey_len < 3 or self.h_keys_down[2]):
            self.h_hotkey_pressed = True

    def on_release(self, key):
        for i in range(len(Preferences.hotkey)):
            if repr(key) == Preferences.hotkey[i]:
                self.keys_down[i] = False

        for i in range(len(Preferences.hotkey_highlight)):
            if repr(key) == Preferences.hotkey_highlight[i]:
                self.h_keys_down[i] = False

        if sum(self.keys_down) == 0 and sum(self.h_keys_down) == 0:
            if self.hotkey_pressed or self.h_hotkey_pressed:
                self.act()
            self.hotkey_pressed = False
            self.h_hotkey_pressed = False

    def start(self):
        listener = keyboard.Listener(
            on_press=self.on_press, on_release=self.on_release)
        listener.start()

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


class HotkeyCaptor:
    def __init__(self):
        self.hotkey_seq = []

    def register_key(self, key):
        if repr(key) not in self.hotkey_seq:
            self.hotkey_seq.append(repr(key))
        if len(self.hotkey_seq) == 3:
            exit()

    def capture_hotkey(self, highlight):
        self.hotkey_seq = []
        listener = keyboard.Listener(
            on_press=self.register_key)
        listener.start()
        time.sleep(3)
        listener.stop()
        if highlight:
            Preferences.hotkey_highlight = self.hotkey_seq
        else:
            Preferences.hotkey = self.hotkey_seq
