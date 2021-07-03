from tkinter import *
from preferences import Preferences
import logging


class GuiWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title('The Ultimate Evaluator')
        self.geometry('400x400')

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

        submit_button = Button(self, text='save', command=self.save_info)
        submit_button.pack()

    def save_info(self):
        print('updated to ' + self.eval_mode.get())
        logging.info('updated to ' + self.eval_mode.get())
        Preferences.mode = self.eval_mode.get()
        Preferences.super_key = self.platform_key
        if self.precision_entry.get():
            Preferences.precision = int(self.precision_entry.get())
        if self.appid_entry.get():
            Preferences.appid = self.appid_entry.get()
        Preferences.write('prefs.txt')
