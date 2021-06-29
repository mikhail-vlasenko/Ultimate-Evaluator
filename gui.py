from tkinter import *
from preferences import Preferences
import logging


class GuiWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title('The Ultimate Evaluator')
        self.geometry('400x400')

        self.eval_mode = StringVar(self, 'basic')
        values = {'Basic': 'basic',
                  'Advanced': 'advanced',
                  'Wolfram': 'wolfram'}

        for (text, value) in values.items():
            Radiobutton(self, text=text, variable=self.eval_mode, value=value, indicator=0,
                        background='light blue').pack(fill=X, ipady=5)

        submit_button = Button(self, text='update', command=self.update_info)
        submit_button.pack()

    def update_info(self):
        print('updated to ' + self.eval_mode.get())
        logging.info('updated to ' + self.eval_mode.get())
        Preferences.mode = self.eval_mode.get()
