from simpleeval import simple_eval
import math
import requests
from bs4 import BeautifulSoup
from preferences import Preferences
import logging
from cleaner import Cleaner


class Evaluator:
    @staticmethod
    def map_brackets(text):
        stack = []
        jump_list = [0] * len(text)
        for i in range(len(text)):
            if text[i] == '(':
                stack.append(i)
            elif text[i] == ')':
                j = stack.pop()
                jump_list[j] = i
                jump_list[i] = j
        return jump_list

    @staticmethod
    def simple_eval(text):
        expr, result = Cleaner.full_cleanup(text, False, False)
        logging.debug(f'evaluating with simple\n{expr}')
        value = simple_eval(expr)
        if int(value) == value:
            value = int(value)
        result += str(value)
        return result

    @staticmethod
    def advanced_eval_wrapper(text):
        text, result = Cleaner.full_cleanup(text, True, False)
        value = Evaluator.advanced_eval(text, Evaluator.map_brackets(text))
        if int(value) == value:
            value = int(value)
        return result + str(value)

    @staticmethod
    def advanced_eval(text, jump_list, substring_start=0):
        logging.debug(f'evaluating, advanced called with\n{text}')
        simplified = ''
        simplified_last = 0
        i = 0
        while i < len(text):
            if text[i].isalpha():
                simplified += text[simplified_last:i]
                func = ''
                j = i
                while text[j] != '(':
                    func += text[j]
                    j += 1
                substring = text[j+1:jump_list[substring_start + j] - substring_start]
                sub_res = Evaluator.advanced_eval(substring, jump_list, substring_start+j+1)
                simplified += str(Evaluator.eval_func(func, sub_res))
                i = jump_list[substring_start + j]
                simplified_last = i + 1
            i += 1
        if simplified == '':
            return simple_eval(text)
        return simple_eval(simplified)

    @staticmethod
    def eval_func(func, number):
        if func == 'ln':
            return math.log(number)
        if func == 'log2':
            return math.log2(number)
        if func == 'sin':
            return math.sin(number)
        if func == 'cos':
            return math.cos(number)

    @staticmethod
    def wolfram_eval(text):
        text, result = Cleaner.full_cleanup(text, True, True)
        response = requests.get(f'https://api.wolframalpha.com/v2/query?input={text}&appid={Preferences.appid}')
        soup = BeautifulSoup(response.content, 'html.parser')
        plaintext = soup.get_text()
        fields = list(filter(None, plaintext.split('\n')))
        answer = fields[1]
        return result + answer
