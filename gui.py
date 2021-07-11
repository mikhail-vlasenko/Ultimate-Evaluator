from tkinter import *
from preferences import Preferences
import logging
import webbrowser
from controller import HotkeyCaptor


class GuiWindow(Tk):
    def __init__(self):
        super().__init__()
        self.captor = HotkeyCaptor()
        self.title('The Ultimate Evaluator')
        self.geometry('500x500')

        self.eval_mode = StringVar(self, Preferences.mode)
        values = {'Basic': 'basic',
                  'Advanced': 'advanced',
                  'Wolfram': 'wolfram'}

        for (text, value) in values.items():
            Radiobutton(self, text=text, variable=self.eval_mode, value=value).pack()

        Label(self, text="Decimal places:").pack()
        self.precision_entry = Entry(self)
        self.precision_entry.insert(END, str(Preferences.precision))
        self.precision_entry.pack()

        Label(self, text="Wolfram appid:").pack()
        self.appid_entry = Entry(self)
        self.appid_entry.insert(END, str(Preferences.appid))
        self.appid_entry.pack()

        self.platform_key = StringVar(self, Preferences.super_key)
        Radiobutton(self, text='Windows', variable=self.platform_key, value='ctrl').pack()
        Radiobutton(self, text='Mac OS', variable=self.platform_key, value='command').pack()

        submit_button = Button(self, text='Save', command=self.save_info)
        submit_button.pack()

        self.hotkey_main = StringVar(self, f'Main hotkey: {Preferences.hotkey}')
        Label(self, textvariable=self.hotkey_main).pack()
        hotkey_button = Button(self, text='Set main hotkey', command=self.get_hotkey)
        hotkey_button.pack()

        self.hotkey_hl = StringVar(self, f'Highlight hotkey: {Preferences.hotkey_highlight}')
        Label(self, textvariable=self.hotkey_hl).pack()
        hotkey_button2 = Button(self, text='Set highlight hotkey', command=lambda: self.get_hotkey(True))
        hotkey_button2.pack()

        help_link = Label(self, text='Help', fg="blue")
        help_link.bind("<Button-1>", lambda e: webbrowser.open_new(
            'https://github.com/mikhail-vlasenko/Ultimate-Evaluator/blob/master/README.md'))
        help_link.pack()

    def save_info(self):
        print('updated to ' + self.eval_mode.get())
        logging.info('updated to ' + self.eval_mode.get())
        Preferences.mode = self.eval_mode.get()
        Preferences.super_key = self.platform_key.get()
        if self.precision_entry.get():
            Preferences.precision = int(self.precision_entry.get())
        if self.appid_entry.get():
            Preferences.appid = self.appid_entry.get()
        Preferences.write('prefs.txt')

    def get_hotkey(self, highlight=False):
        self.captor.capture_hotkey(highlight)
        self.save_info()
        self.hotkey_main.set(f'Main hotkey: {Preferences.hotkey}')
        self.hotkey_hl.set(f'Highlight hotkey: {Preferences.hotkey_highlight}')
