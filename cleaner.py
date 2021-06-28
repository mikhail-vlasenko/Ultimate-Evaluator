import re


class Cleaner:
    @staticmethod
    def remove_letters(text):
        return re.sub(r'[a-zA-Z]', '', text)

    @staticmethod
    def remove_symbols(text, keep_comma_fact):
        text = re.sub(r'\^', '**', text)
        spaces = re.compile('[ \t\n:?<>]')
        text = re.sub(spaces, '', text)
        if not keep_comma_fact:
            text = re.sub(r'[,!]', '', text)
        return text

    @staticmethod
    def add_equals(text):
        result = ' = '
        if text == '':
            return '', ''
        if text[-1] == '=':
            result = ''
            text = text[:-1]
        return text, result

    @staticmethod
    def fix_percents(text):
        percent = re.compile('[0-9]*[.]?[0-9]+%')
        percents = re.findall(percent, text)
        for p in percents:
            number = float(p[:-1]) / 100
            text = text.replace(p, str(number))
        return text

    @staticmethod
    def full_cleanup(text, keep_letters, keep_comma_fact):
        text, result = Cleaner.add_equals(Cleaner.remove_symbols(text, keep_comma_fact))
        text = Cleaner.fix_percents(text)
        if keep_letters:
            return text, result
        return Cleaner.remove_letters(text), result
