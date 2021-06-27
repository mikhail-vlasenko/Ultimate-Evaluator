from simpleeval import simple_eval
import re


class Evaluator:
    @staticmethod
    def beautify(text):
        text = re.sub(r'[a-zA-Z]', '', text)
        return text

    @staticmethod
    def evaluate(text):
        print(f'initial text\n{text}')
        result = ' = '
        spaces = re.compile('[ \t\n,:?!<>]')
        text = re.sub(spaces, '', text)
        if text == '':
            return ''
        if text[-1] == '=':
            result = ''
            text = text[:-1]
        expr = Evaluator.beautify(text)
        print(f'evaluating\n{expr}')
        result += str(simple_eval(expr))
        return result
