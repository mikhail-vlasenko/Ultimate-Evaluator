import re


class Cleaner:
    @staticmethod
    def remove_letters(text):
        return re.sub(r'[a-zA-Z]', '', text)

    @staticmethod
    def remove_symbols(text, keep_fact, keep_comma):
        text = re.sub(r'\^', '**', text)
        spaces = re.compile('[ \t\n:?<>|{}]')
        text = re.sub(spaces, '', text)
        if not keep_fact:
            text = re.sub(r'!', '', text)
        if not keep_comma:
            text = re.sub(r',', '', text)
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
        return text.replace('%', '/100')

    @staticmethod
    def full_cleanup(text, keep_fact, keep_letters, keep_comma):
        text, result = Cleaner.add_equals(Cleaner.remove_symbols(text, keep_fact, keep_comma))
        text = Cleaner.fix_percents(text)
        if keep_letters:
            return text, result
        return Cleaner.remove_letters(text), result
