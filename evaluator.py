from simpleeval import simple_eval
import re
import math


class Evaluator:
    @staticmethod
    def remove_letters(text):
        text = re.sub(r'[a-zA-Z]', '', text)
        return text

    @staticmethod
    def add_equals(text):
        result = ' = '
        spaces = re.compile('[ \t\n,:?!<>]')
        text = re.sub(spaces, '', text)
        if text == '':
            return '', ''
        if text[-1] == '=':
            result = ''
            text = text[:-1]
        return text, result

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
    def evaluate(text):
        print(f'initial text\n{text}')
        text, result = Evaluator.add_equals(text)
        expr = Evaluator.remove_letters(text)
        print(f'evaluating\n{expr}')
        result += str(simple_eval(expr))
        return result

    @staticmethod
    def advanced_eval_wrapper(text):
        text, result = Evaluator.add_equals(text)
        return result + str(Evaluator.advanced_eval(text, Evaluator.map_brackets(text)))

    @staticmethod
    def advanced_eval(text, jump_list, substring_start=0):
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
