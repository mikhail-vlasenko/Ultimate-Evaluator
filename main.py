from controller import Controller
import logging


if __name__ == '__main__':
    logging.basicConfig(filename='evaluator.log', level=logging.DEBUG)
    controller = Controller()
    controller.start()
