from simpleeval import simple_eval


class Evaluator:
    @staticmethod
    def evaluate(text):
        return simple_eval(text)
